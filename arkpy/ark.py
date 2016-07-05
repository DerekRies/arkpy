"""
Collection of file readers and writers for some of the Ark: Survival Evolved
file types.
"""

import utils

from binary import BinaryStream


def read_pair(stream):
  name = stream.readNullTerminatedString()
  typeof = stream.readNullTerminatedString()
  return (name, typeof)

def read_variable_data(stream):
  pair = read_pair(stream)
  # print pair
  if pair[1] == 'FloatProperty':
    stream.readBytes(8)
    float_value = stream.readFloat()
    return (pair[0], float_value)
  elif pair[1] == 'ArrayProperty':
    stream.readBytes(8)
    array = []
    array_type = stream.readNullTerminatedString()
    array_length = stream.readInt32()
    for i in xrange(array_length):
      array.append(stream.readFloat())
    return (pair[0], array)
  return (None, None)

class ArkCharacterSetting:
  """
  A Character preset/template that you can use when you create new
  characters to make the same character (visually)
  """
  def __init__(self, name='unnamed'):
    self.name = name
    self.header = {
      'version': 0,
      'strings': []
    }
    self.character_setting = {
      'BodyColorSliderValue': 0.0,
      'HairColorSliderValue': 0.0,
      'EyeColorSliderValue': 0.0,
      'BoneModifierSliderValues': [0.5] * 22
    }

  @classmethod
  def from_file(cls, file_path):
    preset = cls()
    preset.name = utils.get_file_name(file_path)
    with open(file_path, 'rb') as ifile:
      stream = BinaryStream(ifile)

      # Header portion -----------------------------------
      preset.header['version'] = stream.readInt32()
      stream.readBytes(16)
      preset.header['strings'].append(stream.readNullTerminatedString())
      stream.readBytes(4)
      # Guessing that this `04 00 00 00` refers to how many strings are
      # to follow. If not, then these bytes are unknown and there are
      # just 4 strings following regardless
      for i in xrange(stream.readInt32()):
        preset.header['strings'].append(stream.readNullTerminatedString())
      # End of Header portion ----------------------------

      # Unknown Bytes ------------------------------------
      stream.readBytes(12)
      unknown_bytes = stream.readInt64()
      # End of Unknown Bytes -----------------------------

      # Start of Structured Data -------------------------
      read_pair(stream)
      structprop_permutation_value = stream.readInt64()
      stream.readNullTerminatedString()
      while True:
        data = read_variable_data(stream)
        if data[0] is not None:
          preset.character_setting[data[0]] = data[1]
        else:
          break
      # End of Structured Data ---------------------------

    return preset
