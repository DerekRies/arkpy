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


class BaseProperty:
  def __init__(self, value=None):
    print 'Base Property init'
    self.value=value
  def __repr__(self):
    return str(self.value)
  def __str__(self):
    return str(self.value)


class BaseStruct:
  def __init__(self, size=None):
    self.data = {}
    self.size = 0
  # def __repr__(self):
  #   return json.dumps(self.data)
  # def __str__(self):
  #   return json.dumps(self.data)


class StringProperty:
  def __init__(self, value=''):
    self.value = value


class ArrayProperty:
  def __init__(self, value=[], type='IntProperty'):
    self.value = value


class FloatProperty:
  def __init__(self, value=0.0):
    self.value = value


class DoubleProperty:
  def __init__(self, value=0.0):
    self.value = value


class Int16Property:
  def __init__(self, value=0):
    self.value = value


class UInt16Property:
  def __init__(self, value=0):
    self.value = value


class IntProperty:
  def __init__(self, value=0):
    self.value = value


class UIntProperty:
  def __init__(self, value=0):
    self.value = value


class Int64Property:
  def __init__(self, value=0):
    self.value = value


class UInt64Property(BaseProperty):
  def __init__(self, value=0, stream=None):
    BaseProperty.__init__(self, value=value)
    self.value = value
    if stream is not None:
      stream.readBytes(8)
      self.value = stream.readUInt64()


class BoolProperty:
  def __init__(self, value=True):
    self.value = value


def load_struct(stream):
  size = stream.readInt64()
  name = stream.readNullTerminatedString()
  # print size
  struct = STRUCTS[name](size=size, stream=stream)
  return struct

def load_property(stream):
  name, prop_type = stream.read_pair()
  return (name, prop_type, PROPERTIES[prop_type](stream=stream))

# ArkProfile Structures ----------------------------------

class PrimalPlayerDataStruct(BaseStruct):
  def __init__(self, size=0, stream=None):
    BaseStruct.__init__(self, size=size)
    print 'PrimalPlayerDataStruct initialized'
    # self.data = {}
    # self.size = size
    if stream is not None:
      print 'loading from stream'
      name, prop_type, value = load_property(stream)
      self.data[name] = (prop_type, value)
      print self.data

  def __write_to_binary_stream(self, stream):
    pass


class UniqueNetIdRepl:
  def __init__(self, size=0):
    self.size = size

  @classmethod
  def __from_binary_stream(cls, stream):
    pass

  def __write_to_binary_stream(self, stream):
    pass


class PrimalPlayerCharacterConfigStruct:
  def __init__(self, size=0):
    self.size = size

  @classmethod
  def __from_binary_stream(cls, stream):
    pass

  def __write_to_binary_stream(self, stream):
    pass


class LinearColor:
  def __init__(self, size=0, r=0.0, g=0.0, b=0.0, a=1.0):
    self.size = size
    self.r = r
    self.g = g
    self.b = b
    self.a = a

  @classmethod
  def __from_binary_stream(cls, stream):
    pass

  def __write_to_binary_stream(self, stream):
    pass


class PrimalPersistentCharacterStatsStruct:
  def __init__(self, size=0):
    self.size = size

  @classmethod
  def __from_binary_stream(cls, stream):
    pass

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
  'StringProperty': StringProperty,
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