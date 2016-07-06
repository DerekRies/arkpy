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

from binary import BinaryStream



class PrimalPlayerDataStruct:
  def __init__(self):
    pass

  @classmethod
  def __from_binary_stream(cls, stream):
    pass


class UniqueNetIdRepl:
  def __init__(self):
    pass

  @classmethod
  def __from_binary_stream(cls, stream):
    pass


class PrimalPlayerCharacterConfigStruct:
  def __init__(self):
    pass

  @classmethod
  def __from_binary_stream(cls, stream):
    pass


class LinearColor:
  def __init__(self, r=0.0, g=0.0, b=0.0, a=1.0):
    self.r = r
    self.g = g
    self.b = b
    self.a = a

  @classmethod
  def __from_binary_stream(cls, stream):
    pass


class PrimalPersistentCharacterStatsStruct:
  def __init__(self):
    pass

  @classmethod
  def __from_binary_stream(cls, stream):
    pass
