"""
arktypes is a collection of data structures used in the Ark: Survival
Evolved file formats. This includes subclasses of StructProperty as
well as the primitives used like FloatProperty or IntProperty because
in the file formats the usage of these primitives isn't the typical
bytesize of type + 1 Byte for identifier. Instead most of the primitives
are identified by string, and then have 8 bytes between the type string
and the value, which is usually the size of the structure (4 bytes),
the index (another 4 bytes).
"""

import random
import utils
import json

from binary import BinaryStream

debug = True
# debug = False


def load_struct(stream):
  size = stream.readInt32()
  index = stream.readInt32()
  name = stream.readNullTerminatedString()
  # print size
  # print name
  # struct_to_use = STRUCTS.get(name, PrimalPlayerDataStruct)
  # struct = struct_to_use(size=size, stream=stream)
  struct = STRUCTS[name](size=size, stream=stream)
  struct.index = index
  return struct

def load_property(stream):
  name, prop_type = stream.read_pair()
  # print (name, prop_type)
  if prop_type == 'StructProperty':
    return (name, prop_type, load_struct(stream))
  else:
    return (name, prop_type, PROPERTIES[prop_type](stream=stream))


class BaseProperty():
  def __init__(self, value=None):
    # print 'Base Property init'
    self.value=value
    self.index = 0
    self.size = 0
  # def __repr__(self):
  #   return str(self.value)
  # def __str__(self):
  #   return str(self.value)

  def set(self, value):
    self.value = value


class BaseStruct:
  def __init__(self, size=None):
    self.data = {}
    self.size = 0
    self.index = 0

  def get(self, key):
    return self.data[key]

  def load_and_set_next_property(self, stream):
    """
    Reads and automatically sets the next property value to
    the appropriate field on the data dict of this struct. Since
    some fields in Ark File formats use the same name, but are not
    an array, their differentiator is a little Int32 index field.
    """

    # TODO: Making Default values already instantiated on structs
    # so you can assume any index-based values like BodyColor,
    # BoneModifiers, and LevelUps is already a list with default values
    # Just go to the index of that list and update it with the now
    # read value.

    name, prop_type, value = load_property(stream)
    if self.data.get(name, None) is not None:
      if isinstance(self.data.get(name, None), list):
        if len(self.data[name]) == 0:
          self.data[name].append(value)
        else:
          self.data[name][value.index] = value
      else:
        self.data[name] = value
      # first_item = self.data.get(name, None)
      # if first_item is None:
      #   self.data[name] = []
      # elif isinstance(first_item, list) is False:
      #   self.data[name] = [first_item]
      # self.data[name].append(value)
    else:
      self.data[name] = value
    if debug:
      print '----------------------------------------'
      print "Struct Type: %s" % self.__class__.__name__
      print self.data
      print '----------------------------------------'
    # print value.index
  # def __repr__(self):
  #   return json.dumps(self.data)
  # def __str__(self):
  #   return json.dumps(self.data)


class StrProperty(BaseProperty):
  def __init__(self, value='', stream=None):
    BaseProperty.__init__(self)
    self.value = str(value)
    self.size = 5 + len(value)
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.value = stream.readNullTerminatedString()

  def set(self, value):
    self.value = str(value)
    self.calc_size()

  def calc_size(self):
    # 4 Bytes for the Int32 specifying length
    # N Bytes for the string's characters
    # 1 NULL Byte to terminate the string
    self.size = 5 + len(self.value)
    return self.size

  def __repr__(self):
    return '<StrProperty> %s' % self.value


class ArrayProperty(BaseProperty):
  def __init__(self, child_type='IntProperty', stream=None):
    # print 'MAKING AN ARRAY PROPERTY!!!!!!'
    BaseProperty.__init__(self)
    conversion_table = {
      'IntProperty': stream.readInt32,
      'UIntProperty': stream.readUInt32,
      'UInt32Property': stream.readUInt32,
      'Int16Property': stream.readInt16,
      'UInt16Property': stream.readUInt16,
      'Int64Property': stream.readInt64,
      'UInt64Property': stream.readUInt64,
      'FloatProperty': stream.readFloat,
      'DoubleProperty': stream.readDouble,
      'StrProperty': stream.readNullTerminatedString,
      'ObjectProperty': stream.readNullTerminatedString,
    }
    self.value = []
    # An ArrayProperty's size is not the length of items
    # It is the size of the array values in Bytes like every other
    # property/struct
    self.size = 4
    self.child_type = child_type
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.child_type = stream.readNullTerminatedString()
      self.length = stream.readInt32()
      # print 'SIZE: ' + str(self.size)
      # print 'LENGTH: ' + str(self.length)
      for i in xrange(self.length):
        # print 'ITEM: ' + str(i)
        # print stream.readNullTerminatedString()
        if self.child_type == 'ObjectProperty':
          stream.readInt32()
          value = stream.readNullTerminatedString()
          # print value
        else:
          value = conversion_table[self.child_type]()
        self.value.append(value)
        # if self.child_type == 'ObjectProperty' and i != self.length - 1:
          # Object Properties are separated by 01 00 00 00

  def __repr__(self):
    return "[]<%s>(%s)" % (self.child_type, self.length)
    # return "[" + ", ".join(str(x) for x in self.value) + "]<%s>" % self.child_type

  def calc_size(self):
    # 4 Bytes for length of the array
    # Sum of all child sizes
    pass


class ByteProperty(BaseProperty):
  def __init__(self, value=0, stream=None):
    BaseProperty.__init__(self)
    self.value = value
    self.size = 4
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      # No idea why there's a junk "None" inserted here
      stream.readNullTerminatedString()
      self.value = stream.readChar()

  def set(self, value=0):
    self.value = int(value)

  def __repr__(self):
    return '<ByteProperty> %s' % self.value



class ObjectProperty(BaseProperty):
  def __init__(self, value='', stream=None):
    BaseProperty.__init__(self)
    self.set(value)
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      # No idea what this is, it's always 01 00 00 00 in the
      # ObjectProperties I've seen. Maybe it's an identifier
      # for the type of data to follow, like 1=String?
      prefix = stream.readInt32()
      self.value = stream.readNullTerminatedString()

  def set(self, value):
    self.value = value
    self.calc_size()

  def calc_size(self):
    # 4 Bytes for Prefix (01 00 00 00)
    # 4 Bytes for string length
    # N Bytes for N length string
    # 1 NULL Byte to terminate string
    self.size = 9 + len(self.value)

  def _write_to_stream(self, array=False):
    # When not inside of an ArrayProperty the writing of bytes is:
    # 1. Variable Name as NTString
    # 2. ObjectProperty as NTString
    # 3. Size in Bytes as Int32
    # 4. Index as Int32
    # 5. Prefix as Int32
    # 6. Value as NTString
    #
    # However, inside of an ArrayProperty only write:
    # 1. Prefix as Int32
    # 2. Value as NTString
    pass


class FloatProperty(BaseProperty):
  def __init__(self, value=0.0, stream=None):
    BaseProperty.__init__(self)
    self.value = value
    self.size = 4
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.value = stream.readFloat()

  def set(self, value=0.0):
    self.value = float(value)

  def __repr__(self):
    return '<FloatProperty> %s' % self.value


class DoubleProperty(BaseProperty):
  def __init__(self, value=0.0, stream=None):
    BaseProperty.__init__(self)
    self.value = value
    self.size = 8
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.value = stream.readDouble()


class Int16Property(BaseProperty):
  def __init__(self, value=0, stream=None):
    BaseProperty.__init__(self)
    self.value = value
    self.size = 2
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.value = stream.readInt16()

  def set(self, value=0):
    self.value = int(value)

  def __repr__(self):
    return '<Int16Property> %s' % self.value


class UInt16Property(BaseProperty):
  def __init__(self, value=0, stream=None):
    BaseProperty.__init__(self)
    self.value = value
    self.size = 2
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.value = stream.readUInt16()

  def set(self, value=0):
    self.value = int(value)

  def __repr__(self):
    return '<UInt16Property> %s' % self.value


class IntProperty(BaseProperty):
  def __init__(self, value=0, stream=None):
    BaseProperty.__init__(self)
    self.value = value
    self.size = 4
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.value = stream.readInt32()

  def set(self, value=0):
    self.value = int(value)

  def __repr__(self):
    return '<IntProperty> %s' % self.value


class UIntProperty(BaseProperty):
  def __init__(self, value=0, stream=None):
    BaseProperty.__init__(self)
    self.value = value
    self.size = 4
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.value = stream.readUInt32()

  def set(self, value=0):
    self.value = int(value)

  def __repr__(self):
    return '<UInt32Property> %s' % self.value


class Int64Property(BaseProperty):
  def __init__(self, value=0, stream=None):
    BaseProperty.__init__(self)
    self.value = value
    self.size = 8
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.value = stream.readInt64()

  def set(self, value=0):
    self.value = int(value)

  def __repr__(self):
    return '<Int64Property> %s' % self.value


class UInt64Property(BaseProperty):
  def __init__(self, value=0, stream=None):
    BaseProperty.__init__(self, value=value)
    self.value = value
    self.size = 8
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.value = stream.readUInt64()

  def set(self, value=0):
    self.value = int(value)

  def __repr__(self):
    return '<UInt64Property> %s' % self.value


class BoolProperty(BaseProperty):
  def __init__(self, value=True, stream=None):
    BaseProperty.__init__(self)
    self.value = value
    if stream is not None:
      garbage = stream.readInt32()
      self.index = stream.readInt32()
      self.value = bool(stream.readChar())

  def set(self, value=True):
    self.value = bool(value)

  def __repr__(self):
    return '<BoolProperty> %s' % self.value


# ArkProfile Structures ----------------------------------

class PrimalPlayerDataStruct(BaseStruct):
  def __init__(self, size=0, stream=None):
    BaseStruct.__init__(self, size=size)
    # print 'PrimalPlayerDataStruct initialized'
    # self.data = {}
    self.size = size

    # Default Values
    self.data['PlayerDataID'] = UInt64Property(value=0)
    self.data['UniqueID'] = UniqueNetIdRepl()
    self.data['SavedNetworkAddress'] = StrProperty()
    self.data['PlayerName'] = StrProperty()
    self.data['bFirstSpawned'] = BoolProperty()
    cs = 'MyPlayerCharacterConfig'
    self.data[cs] = PrimalPlayerCharacterConfigStruct()
    ss = 'MyPersistentCharacterStats'
    self.data[ss] = PrimalPersistentCharacterStatsStruct()
    self.data['PlayerDataVersion'] = IntProperty(value=1)

    if stream is not None:
      # print 'loading from stream'
      while stream.peek(stream.readNullTerminatedString) != 'None':
        self.load_and_set_next_property(stream)
      stream.readNullTerminatedString()

  def __write_to_binary_stream(self, stream):
    pass


class UniqueNetIdRepl(BaseStruct):
  def __init__(self, size=0, stream=None):
    BaseStruct.__init__(self, size=size)
    self.size = size
    self.value = None
    if stream is not None:
      stream.readInt32()
      self.value = stream.readNullTerminatedString()

  def set(self, value=''):
    self.value = str(value)

  def __write_to_binary_stream(self, stream):
    pass

  def __repr__(self):
    return str(self.__class__.__name__) + ': ' + str(self.value)


class PrimalPlayerCharacterConfigStruct(BaseStruct):
  def __init__(self, size=0, stream=None):
    BaseStruct.__init__(self, size=size)
    self.size = size

    # Default Values
    self.data['BodyColors'] = [LinearColor()] * 3
    self.data['RawBoneModifiers'] = [FloatProperty(value=0.5)] * 22
    self.data['bIsFemale'] = BoolProperty(value=False)
    self.data['PlayerCharacterName'] = StrProperty()
    self.data['PlayerSpawnRegionIndex'] = IntProperty()

    if stream is not None:
      # Structs with multiple values end with None
      while stream.peek(stream.readNullTerminatedString) != 'None':
        self.load_and_set_next_property(stream)
      # Remember to read the None to advance position past it when done
      stream.readNullTerminatedString()

  def __write_to_binary_stream(self, stream):
    pass


class LinearColor(BaseStruct):
  def __init__(self, size=16, r=0.0, g=0.0, b=0.0, a=1.0, stream=None):
    BaseStruct.__init__(self)
    self.size = 16
    self.r = r
    self.g = g
    self.b = b
    self.a = a
    if stream is not None:
      self.r = stream.readFloat()
      self.g = stream.readFloat()
      self.b = stream.readFloat()
      self.a = stream.readFloat()

  def __write_to_binary_stream(self, stream):
    pass

  def __repr__(self):
    return "(R: %s, G: %s, B: %s, A: %s)" % (self.r, self.g, self.b, self.a)

  def set(self, r=0.0, g=0.0, b=0.0, a=1.0):
    self.r = float(r)
    self.g = float(g)
    self.b = float(b)
    self.a = float(a)



class PrimalPersistentCharacterStatsStruct(BaseStruct):
  def __init__(self, size=0, stream=None):
    BaseStruct.__init__(self)
    self.size = size

    # Default Values
    level_up_string = 'CharacterStatusComponent_NumberOfLevelUpPointsApplied'
    exp_string = 'CharacterStatusComponent_ExperiencePoints'
    levels_string = 'CharacterStatusComponent_ExtraCharacterLevel'
    self.data[levels_string] = UInt16Property()
    self.data[exp_string] = FloatProperty()
    self.data['PlayerState_TotalEngramPoints'] = IntProperty()
    self.data[level_up_string] = [ByteProperty()] * 12
    self.data['PlayerState_DefaultItemSlotClasses'] = [None] * 10

    if stream is not None:
      while stream.peek(stream.readNullTerminatedString) != 'None':
        self.load_and_set_next_property(stream)
      stream.readNullTerminatedString()

  def __write_to_binary_stream(self, stream):
    pass


# End of ArkProfile Structures ----------------------------

PROPERTIES = {
  'IntProperty': IntProperty,
  'UIntProperty': UIntProperty,
  'UInt32Property': UIntProperty,
  'Int16Property': Int16Property,
  'UInt16Property': UInt16Property,
  'Int64Property': Int64Property,
  'UInt64Property': UInt64Property,
  'FloatProperty': FloatProperty,
  'DoubleProperty': DoubleProperty,
  'StrProperty': StrProperty,
  'BoolProperty': BoolProperty,
  'ArrayProperty': ArrayProperty,
  'ByteProperty': ByteProperty,
  'ObjectProperty': ObjectProperty,
}
STRUCTS = {
  'PrimalPlayerDataStruct': PrimalPlayerDataStruct,
  'UniqueNetIdRepl': UniqueNetIdRepl,
  'PrimalPlayerCharacterConfigStruct': PrimalPlayerCharacterConfigStruct,
  'LinearColor': LinearColor,
  'PrimalPersistentCharacterStatsStruct': PrimalPersistentCharacterStatsStruct
}