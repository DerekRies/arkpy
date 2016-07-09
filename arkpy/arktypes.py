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


class BaseProperty:
  def __init__(self, value=None):
    # print 'Base Property init'
    self.value=value
    self.index = 0
    self.size = 0
  def __repr__(self):
    return str(self.value)
  def __str__(self):
    return str(self.value)

  def set(self, val):
    self.value = val


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
    name, prop_type, value = load_property(stream)
    if value.index != 0:
      first_item = self.data.get(name, None)
      if first_item is None:
        self.data[name] = []
      elif isinstance(first_item, list) is False:
        self.data[name] = [first_item]
      self.data[name].append(value)
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
    self.value = value
    self.size = 4
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.value = stream.readNullTerminatedString()

  def __repr__(self):
    return self.value


class ArrayProperty(BaseProperty):
  def __init__(self, value=[], child_type='IntProperty', stream=None):
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
    self.value = value
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
          print value
        else:
          value = conversion_table[self.child_type]()
        self.value.append(value)
        # if self.child_type == 'ObjectProperty' and i != self.length - 1:
          # Object Properties are separated by 01 00 00 00

  def __repr__(self):
    return "[]<%s>(%s)" % (self.child_type, self.length)
    # return "[" + ", ".join(str(x) for x in self.value) + "]<%s>" % self.child_type


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


class ObjectProperty(BaseProperty):
  def __init__(self, value=0.0, stream=None):
    BaseProperty.__init__(self)
    self.value = value
    self.size = 4
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      # No idea what this is, it's always 01 00 00 00 in the
      # ObjectProperties I've seen. Maybe it's an identifier
      # for the type of data to follow, like 1=String?
      prefix = stream.readInt32()
      self.value = stream.readNullTerminatedString()


class FloatProperty(BaseProperty):
  def __init__(self, value=0.0, stream=None):
    BaseProperty.__init__(self)
    self.value = value
    self.size = 4
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.value = stream.readFloat()

  def set(self, val=0.0):
    self.value = float(val)


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


class BoolProperty(BaseProperty):
  def __init__(self, value=True, stream=None):
    BaseProperty.__init__(self)
    self.value = value
    if stream is not None:
      garbage = stream.readInt32()
      self.index = stream.readInt32()
      self.value = bool(stream.readChar())


# ArkProfile Structures ----------------------------------

class PrimalPlayerDataStruct(BaseStruct):
  def __init__(self, size=0, stream=None):
    BaseStruct.__init__(self, size=size)
    print 'PrimalPlayerDataStruct initialized'
    # self.data = {}
    self.size = size
    if stream is not None:
      print 'loading from stream'
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

  def __write_to_binary_stream(self, stream):
    pass

  def __repr__(self):
    return str(self.__class__.__name__) + ': ' + str(self.value)


class PrimalPlayerCharacterConfigStruct(BaseStruct):
  def __init__(self, size=0, stream=None):
    BaseStruct.__init__(self, size=size)
    self.size = size
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


class PrimalPersistentCharacterStatsStruct(BaseStruct):
  def __init__(self, size=0, stream=None):
    BaseStruct.__init__(self)
    self.size = size
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