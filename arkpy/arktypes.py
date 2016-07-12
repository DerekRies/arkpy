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
import itertools

from binary import BinaryStream

debug = True
# debug = False


def load_struct(stream):
  size = stream.readInt32()
  index = stream.readInt32()
  name = stream.readNullTerminatedString()
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
    self.wrapped_size = 0
    self.var_name = ''
    self.included = True

  def set(self, value):
    self.value = value

  def _write_shared_prop_info(self, stream):
    stream.writeNullTerminatedString(self.var_name)
    stream.writeNullTerminatedString(self.__class__.__name__)
    stream.writeInt32(self.size)
    stream.writeInt32(self.index)

  def _calc_inner_size(self):
    return self.size

  def _calc_wrapper_size(self):
    # 5 Bytes for each NTString
    ws = len(self.var_name) + len(self.__class__.__name__) + 10
    # 4 Bytes for two Int32s (innersize, index)
    ws = ws + 8
    return ws

  def _calc_size(self):
    ws = self._calc_wrapper_size()
    self.wrapped_size = ws + self.size
    return self.wrapped_size

  def __repr__(self):
    return '<%s> %s' % (self.__class__.__name__, self.value)


class BaseStruct:
  def __init__(self):
    self.data = {}
    self.size = 0
    self.wrapped_size = 0
    self.index = 0
    self.var_name = ''
    self.included = True

  def get(self, key):
    return self.data[key]

  def set(self, key, value):
    if isinstance(value, list):
      for i in xrange(len(value)):
        value[i].var_name = key
    else:
      value.var_name = key
    self.data[key] = value

  def load_and_set_next_property(self, stream):
    """
    Reads and automatically sets the next property value to
    the appropriate field on the data dict of this struct. Since
    some fields in Ark File formats use the same name, but are not
    an array, their differentiator is a little Int32 index field.
    """
    name, prop_type, value = load_property(stream)
    value.var_name = name
    if self.data.get(name, None) is not None:
      if isinstance(self.data.get(name, None), list):
        if len(self.data[name]) == 0:
          self.data[name].append(value)
        else:
          self.data[name][value.index] = value
      else:
        self.data[name] = value
    else:
      self.data[name] = value
    if debug:
      print '----------------------------------------'
      print "Struct Type: %s" % self.__class__.__name__
      print self.data
      print '----------------------------------------'

  def _calc_inner_size(self):
    size = 0
    for key in self.data:
      if isinstance(self.data[key], list):
        for val in self.data[key]:
          if val.included:
            size = size + val._calc_size()
      else:
        if self.data[key].included:
          # try:
          size = size + self.data[key]._calc_size()
          # except TypeError:
            # print key
    # NTString 'None' Bytes included
    self.size = size + 9
    return self.size

  def _calc_wrapper_size(self):
    # 5 Bytes for each NTString
    ws = len(self.var_name) + len(self.__class__.__name__) + 10
    # 19 Bytes for StructProperty NTString
    ws = ws + 19
    # 4 Bytes for two Int32s (innersize, index)
    ws = ws + 8
    return ws

  def _calc_size(self):
    # A structs size is the sum of all its non-default children's
    # wrapped_sizes.
    # The wrapped size is the size of the value + the bytes for the
    # variable name, variable type, (and sub-type if struct+available)
    self._calc_inner_size()
    ws = self._calc_wrapper_size()
    self.wrapped_size = ws + self.size
    return self.wrapped_size

  def _write_shared_struct_info(self, stream):
    stream.writeNullTerminatedString(self.var_name)
    stream.writeNullTerminatedString('StructProperty')
    stream.writeInt32(self.size)
    stream.writeInt32(self.index)
    stream.writeNullTerminatedString(self.__class__.__name__)


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
    self.size = 5 + len(self.value)

  def _calc_inner_size(self):
    self.size = 5 + len(self.value)
    return self.size

  def _write_to_stream(self, stream, array=False):
    if array == False:
      self._write_shared_prop_info(stream)
    stream.writeNullTerminatedString(self.value)


class ArrayProperty(BaseProperty):
  def __init__(self, child_type='IntProperty', stream=None):
    BaseProperty.__init__(self)
    self.value = []
    # An ArrayProperty's size is not the length of items
    # It is the size of the array values in Bytes like every other
    # property/struct
    self.size = 4
    self.child_type = child_type
    self.length = 0
    if stream is not None:
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
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.child_type = stream.readNullTerminatedString()
      self.length = stream.readInt32()
      for i in xrange(self.length):
        if self.child_type == 'ObjectProperty':
          stream.readInt32()
          value = stream.readNullTerminatedString()
        else:
          value = conversion_table[self.child_type]()
        prop = PROPERTIES[self.child_type](value=value)
        self.value.append(prop)

  def __repr__(self):
    return "[]<%s>(%s)" % (self.child_type, self.length)

  def _calc_inner_size(self):
    print 'Calculating ArrayProperty Inner Size'
    size = 4
    for val in self.value:
      size = size + val._calc_inner_size()
    self.size = size
    return self.size

  def _calc_wrapper_size(self):
    # 5 Bytes for each NTString
    ws = len(self.var_name) + len(self.child_type) + 10
    # 18 Bytes for ArrayProperty NTString
    ws = ws + 18
    # 4 Bytes for two Int32s (innersize, index)
    ws = ws + 8
    return ws

  def _calc_size(self):
    if len(self.value) > 0:
      self._calc_inner_size()
      # Another 18 Bytes for ArrayProperty
      ws = self._calc_wrapper_size()
      self.wrapped_size = ws + self.size
      return self.wrapped_size
    else:
      return 0

  def _write_to_stream(self, stream):
    if len(self.value) > 0:
      stream.writeNullTerminatedString(self.var_name)
      stream.writeNullTerminatedString('ArrayProperty')
      stream.writeInt32(self.size)
      stream.writeInt32(self.index)
      stream.writeNullTerminatedString(self.child_type)
      stream.writeInt32(len(self.value))
      for val in self.value:
        val._write_to_stream(stream, array=True)


class ByteProperty(BaseProperty):
  def __init__(self, value=0, stream=None, index=0):
    BaseProperty.__init__(self)
    self.value = value
    self.index = index
    self.size = 1
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      # No idea why there's a junk "None" inserted here
      stream.readNullTerminatedString()
      self.value = stream.readChar()

  def set(self, value=0):
    self.value = int(value)

  def _calc_size(self):
    ws = self._calc_wrapper_size()
    # NTString 'None' needs to be counted
    ws = ws + 9
    self.wrapped_size = ws + self.size
    return self.wrapped_size

  def _write_to_stream(self, stream, array=False):
    if array == False:
      self._write_shared_prop_info(stream)
    stream.writeNullTerminatedString('None')
    stream.writeChar(self.value)



class ObjectProperty(BaseProperty):
  def __init__(self, value='', stream=None, index=0):
    BaseProperty.__init__(self)
    self.index = index
    self.value = value
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

  def _calc_inner_size(self):
    # 4 Bytes for Prefix (01 00 00 00)
    # 4 Bytes for string length
    # N Bytes for N length string
    # 1 NULL Byte to terminate string
    self.size = 9 + len(self.value)
    return self.size

  def _calc_size(self):
    self._calc_inner_size()
    ws = self._calc_wrapper_size()
    self.wrapped_size = ws + self.size
    return self.wrapped_size

  def _write_to_stream(self, stream, array=False):
    if array == False:
      self._write_shared_prop_info(stream)
    stream.writeInt32(1)
    stream.writeNullTerminatedString(self.value)


class FloatProperty(BaseProperty):
  def __init__(self, value=0.0, stream=None, index=0):
    BaseProperty.__init__(self)
    self.value = value
    self.size = 4
    self.index = index
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.value = stream.readFloat()

  def set(self, value=0.0):
    self.value = float(value)

  def _write_to_stream(self, stream, array=False):
    if array == False:
      self._write_shared_prop_info(stream)
    stream.writeFloat(self.value)


class DoubleProperty(BaseProperty):
  def __init__(self, value=0.0, stream=None):
    BaseProperty.__init__(self)
    self.value = value
    self.size = 8
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.value = stream.readDouble()

  def set(self, value=0.0):
    self.value = float(value)

  def _write_to_stream(self, stream, array=False):
    if array == False:
      self._write_shared_prop_info(stream)
    stream.writeDouble(self.value)


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

  def _write_to_stream(self, stream, array=False):
    if array == False:
      self._write_shared_prop_info(stream)
    stream.writeInt16(self.value)


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

  def _write_to_stream(self, stream, array=False):
    if array == False:
      self._write_shared_prop_info(stream)
    stream.writeUInt16(self.value)


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

  def _write_to_stream(self, stream, array=False):
    if array == False:
      self._write_shared_prop_info(stream)
    stream.writeInt32(self.value)


class UInt32Property(BaseProperty):
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

  def _write_to_stream(self, stream, array=False):
    if array == False:
      self._write_shared_prop_info(stream)
    stream.writeUInt32(self.value)


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

  def _write_to_stream(self, stream, array=False):
    if array == False:
      self._write_shared_prop_info(stream)
    stream.writeInt64(self.value)


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

  def _write_to_stream(self, stream, array=False):
    if array == False:
      self._write_shared_prop_info(stream)
    stream.writeUInt64(self.value)


class BoolProperty(BaseProperty):
  def __init__(self, value=True, stream=None):
    BaseProperty.__init__(self)
    self.value = value
    self.size = 0
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.value = bool(stream.readChar())

  def set(self, value=True):
    self.value = bool(value)

  def _write_to_stream(self, stream, array=False):
    if array == False:
      self._write_shared_prop_info(stream)
    stream.writeBool(self.value)

  def _calc_size(self):
  # BoolPropertys are a bit of a Heisenbug when it comes to
  # their size. When they are written their size value is always
  # 0, but their true size is of course 1 Byte. Because
  # when it comes time for structs and container properties like
  # ObjectProperty or ArrayProperty types to calculate their size
  # there will be 1 more Byte in the file than what the size says
  # it is, because the size and true size don't match.
    ws = self._calc_wrapper_size()
    self.wrapped_size = ws + 1
    return self.wrapped_size


# ArkProfile Structures ----------------------------------

class PrimalPlayerDataStruct(BaseStruct):
  def __init__(self, size=0, stream=None):
    BaseStruct.__init__(self)
    self.size = size
    self.var_name = 'MyData'

    # Default Values
    self.set('PlayerDataID', UInt64Property(value=0))
    self.set('UniqueID', UniqueNetIdRepl())
    self.set('SavedNetworkAddress', StrProperty())
    self.set('PlayerName', StrProperty())
    self.set('bFirstSpawned', BoolProperty())
    cs = 'MyPlayerCharacterConfig'
    self.set(cs, PrimalPlayerCharacterConfigStruct())
    ss = 'MyPersistentCharacterStats'
    self.set(ss, PrimalPersistentCharacterStatsStruct())
    self.set('PlayerDataVersion', IntProperty(value=1))
    self.set('AppIDSet', ArrayProperty(child_type='IntProperty'))
    self.data['AppIDSet'].value.append(IntProperty(value=375350))

    if stream is not None:
      while stream.peek(stream.readNullTerminatedString) != 'None':
        self.load_and_set_next_property(stream)
      stream.readNullTerminatedString()

  def _write_to_stream(self, stream):
    print 'calculating sizes'
    self._calc_size()
    print 'writing player data struct'
    self._write_shared_struct_info(stream)
    self.data['PlayerDataID']._write_to_stream(stream)
    self.data['UniqueID']._write_to_stream(stream)
    self.data['SavedNetworkAddress']._write_to_stream(stream)
    self.data['PlayerName']._write_to_stream(stream)
    self.data['bFirstSpawned']._write_to_stream(stream)
    self.data['MyPlayerCharacterConfig']._write_to_stream(stream)
    self.data['MyPersistentCharacterStats']._write_to_stream(stream)
    self.data['PlayerDataVersion']._write_to_stream(stream)
    self.data['AppIDSet']._write_to_stream(stream)
    stream.writeNullTerminatedString('None')


class UniqueNetIdRepl(BaseStruct):
  def __init__(self, stream=None):
    BaseStruct.__init__(self)
    self.size = 26
    self.value = '00000000000000000'
    if stream is not None:
      stream.readInt32()
      self.value = stream.readNullTerminatedString()

  def set(self, value=''):
    self.value = str(value)

  def _write_to_stream(self, stream):
    self._write_shared_struct_info(stream)
    stream.writeInt32(8)
    stream.writeNullTerminatedString(self.value)

  def __repr__(self):
    return str(self.__class__.__name__) + ': ' + str(self.value)

  def _calc_size(self):
    self.size = len(self.value) + 9
    ws = self._calc_wrapper_size()
    self.wrapped_size = ws + self.size
    return self.wrapped_size


class PrimalPlayerCharacterConfigStruct(BaseStruct):
  def __init__(self, stream=None):
    BaseStruct.__init__(self)
    # Default Values
    # Setting the index values from the loop in the init
    # because EVERY other solution I tried, including closures
    # and seperate method calls resulted in the same scope
    # and assigning the same index value to every single list item
    colors = [LinearColor(index=i) for i in xrange(3)]
    self.set('BodyColors', colors)
    # self.set('BodyColors', [])
    bones = [FloatProperty(value=0.5, index=j) for j in xrange(22)]
    self.set('RawBoneModifiers', bones)
    # self.set('RawBoneModifiers', [])
    self.set('bIsFemale', BoolProperty(value=False))
    self.set('PlayerCharacterName', StrProperty())
    self.set('PlayerSpawnRegionIndex', IntProperty())

    if stream is not None:
      # Structs with multiple values end with None
      while stream.peek(stream.readNullTerminatedString) != 'None':
        self.load_and_set_next_property(stream)
      # Remember to read the None to advance position past it when done
      stream.readNullTerminatedString()

  def _write_to_stream(self, stream):
    self._write_shared_struct_info(stream)
    for color in self.data['BodyColors']:
      color._write_to_stream(stream)
    for bone in self.data['RawBoneModifiers']:
      bone._write_to_stream(stream)
    self.data['bIsFemale']._write_to_stream(stream)
    self.data['PlayerCharacterName']._write_to_stream(stream)
    self.data['PlayerSpawnRegionIndex']._write_to_stream(stream)
    stream.writeNullTerminatedString('None')


class LinearColor(BaseStruct):
  def __init__(self, r=0.0, g=0.0, b=0.0, a=1.0, stream=None, index=0):
    BaseStruct.__init__(self)
    self.size = 16
    self.index = index
    self.r = r
    self.g = g
    self.b = b
    self.a = a
    if stream is not None:
      self.r = stream.readFloat()
      self.g = stream.readFloat()
      self.b = stream.readFloat()
      self.a = stream.readFloat()

  def _calc_size(self):
    ws = self._calc_wrapper_size()
    self.wrapped_size = ws + self.size
    return self.wrapped_size

  def set(self, r=0.0, g=0.0, b=0.0, a=1.0):
    self.r = float(r)
    self.g = float(g)
    self.b = float(b)
    self.a = float(a)

  def __repr__(self):
    return "(R: %s, G: %s, B: %s, A: %s)" % (self.r, self.g, self.b, self.a)

  def _write_to_stream(self, stream):
    self._write_shared_struct_info(stream)
    stream.writeFloat(self.r)
    stream.writeFloat(self.g)
    stream.writeFloat(self.b)
    stream.writeFloat(self.a)



class PrimalPersistentCharacterStatsStruct(BaseStruct):
  def __init__(self, stream=None):
    BaseStruct.__init__(self)

    # Default Values
    levels_string = 'CharacterStatusComponent_ExtraCharacterLevel'
    exp_string = 'CharacterStatusComponent_ExperiencePoints'
    level_up_string = 'CharacterStatusComponent_NumberOfLevelUpPointsApplied'

    self.set(levels_string, UInt16Property())
    self.set(exp_string, FloatProperty())
    self.set('PlayerState_TotalEngramPoints', IntProperty())
    learned_engrams = ArrayProperty(child_type='ObjectProperty')
    self.set('PlayerState_EngramBlueprints', learned_engrams)
    lvlups = [ByteProperty(index=i) for i in xrange(12)]
    self.set(level_up_string, lvlups)
    # self.set(level_up_string, [])
    default_slots = [ObjectProperty(index=i) for i in xrange(10)]
    self.set('PlayerState_DefaultItemSlotClasses', default_slots)
    # self.set('PlayerState_DefaultItemSlotClasses', [])

    if stream is not None:
      while stream.peek(stream.readNullTerminatedString) != 'None':
        self.load_and_set_next_property(stream)
      stream.readNullTerminatedString()

  def _write_to_stream(self, stream):
    self._write_shared_struct_info(stream)
    levels_string = 'CharacterStatusComponent_ExtraCharacterLevel'
    exp_string = 'CharacterStatusComponent_ExperiencePoints'
    level_up_string = 'CharacterStatusComponent_NumberOfLevelUpPointsApplied'
    self.data[levels_string]._write_to_stream(stream)
    self.data[exp_string]._write_to_stream(stream)
    self.data['PlayerState_TotalEngramPoints']._write_to_stream(stream)
    self.data['PlayerState_EngramBlueprints']._write_to_stream(stream)
    for lvlup in self.data[level_up_string]:
      lvlup._write_to_stream(stream)
    for slot in self.data['PlayerState_DefaultItemSlotClasses']:
      slot._write_to_stream(stream)
    stream.writeNullTerminatedString('None')


# End of ArkProfile Structures ----------------------------

PROPERTIES = {
  'IntProperty': IntProperty,
  'UIntProperty': UInt32Property,
  'UInt32Property': UInt32Property,
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