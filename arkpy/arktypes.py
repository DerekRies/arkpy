"""
arktypes is a collection of data structures used in the Ark: Survival
Evolved file formats. This includes subclasses of StructProperty as
well as the primitives used like FloatProperty or IntProperty because
in the file formats the usage of these primitives isn't the typical
bytesize of type + 1 Byte for identifier. Instead most of the primitives
are identified by string, and then have 8 bytes between the type string
and the value, which is usually just 8 padding bytes, but in some cases
contains an identifier which is used by some of the parent structs.
"""

import random
import utils
import json

from binary import BinaryStream


def load_struct(stream):
  size = stream.readInt32()
  index = stream.readInt32()
  name = stream.readNullTerminatedString()
  # print size
  # print name
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


class BaseStruct:
  def __init__(self, size=None):
    self.data = {}
    self.size = 0
    self.index = 0

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
      self.data[name].append((prop_type, value))
    else:
      self.data[name] = (prop_type, value)
    print self.data
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


class ArrayProperty:
  def __init__(self, value=[], type='IntProperty'):
    self.value = value


class FloatProperty(BaseProperty):
  def __init__(self, value=0.0, stream=None):
    BaseProperty.__init__(self)
    self.value = value
    self.size = 4
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.value = stream.readFloat()


class DoubleProperty:
  def __init__(self, value=0.0):
    self.value = value
    self.size = 8


class Int16Property:
  def __init__(self, value=0):
    self.value = value
    self.size = 2


class UInt16Property:
  def __init__(self, value=0):
    self.value = value
    self.size = 2


class IntProperty:
  def __init__(self, value=0):
    self.value = value
    self.size = 4


class UIntProperty:
  def __init__(self, value=0):
    self.value = value
    self.size = 4


class Int64Property:
  def __init__(self, value=0):
    self.value = value
    self.size = 8


class UInt64Property(BaseProperty):
  def __init__(self, value=0, stream=None):
    BaseProperty.__init__(self, value=value)
    self.value = value
    self.size = 8
    if stream is not None:
      self.size = stream.readInt32()
      self.index = stream.readInt32()
      self.value = stream.readUInt64()


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
      self.load_and_set_next_property(stream)
      # print '---------------------------------'
      self.load_and_set_next_property(stream)
      # print '---------------------------------'
      self.load_and_set_next_property(stream)
      # print '---------------------------------'
      self.load_and_set_next_property(stream)
      # print '---------------------------------'

      self.load_and_set_next_property(stream)
      # print '---------------------------------'

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
      # Colors
      self.load_and_set_next_property(stream)
      self.load_and_set_next_property(stream)
      self.load_and_set_next_property(stream)
      self.load_and_set_next_property(stream)
      self.load_and_set_next_property(stream)


  def __write_to_binary_stream(self, stream):
    pass


class LinearColor(BaseStruct):
  def __init__(self, size=0, r=0.0, g=0.0, b=0.0, a=1.0, stream=None):
    BaseStruct.__init__(self, size=size)
    self.size = size
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


class PrimalPersistentCharacterStatsStruct:
  def __init__(self, size=0, stream=None):
    self.size = size

  def __write_to_binary_stream(self, stream):
    pass

# End of ArkProfile Structures ----------------------------

PROPERTIES = {
  'IntProperty': IntProperty,
  'UIntProperty': UIntProperty,
  'Int16Property': Int16Property,
  'UInt16Property': UInt16Property,
  'Int64Property': Int64Property,
  'UInt64Property': UInt64Property,
  'FloatProperty': FloatProperty,
  'DoubleProperty': DoubleProperty,
  'StrProperty': StrProperty,
  'BoolProperty': BoolProperty,
  'ArrayProperty': ArrayProperty,
}
STRUCTS = {
  'PrimalPlayerDataStruct': PrimalPlayerDataStruct,
  'UniqueNetIdRepl': UniqueNetIdRepl,
  'PrimalPlayerCharacterConfigStruct': PrimalPlayerCharacterConfigStruct,
  'LinearColor': LinearColor,
  'PrimalPersistentCharacterStatsStruct': PrimalPersistentCharacterStatsStruct
}