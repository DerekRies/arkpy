"""
Collection of file readers and writers for some of the Ark: Survival Evolved
file types.
"""

import random
import utils
import arktypes

from binary import BinaryStream


# def stream.read_pair():
#   name = stream.readNullTerminatedString()
#   typeof = stream.readNullTerminatedString()
#   return (name, typeof)

BoneModifierIndices = {
  'Head Size': 0,
  'Upper Face Size': 15,
  'Lower Face Size': 16,
  'Head Width': 19,
  'Head Height': 18,
  'Head Depth': 20,
  'Hand': 8,
  'Arm Length': 5,
  'Upper Arm': 6,
  'Lower Arm': 7,
  'Neck Size': 1,
  'Neck Length': 2,
  'Chest': 3,
  'Shoulders': 4,
  'Hip': 13,
  'Torso Width': 14,
  'Torso Height': 21,
  'Torso Depth': 17,
  'Leg Length': 9,
  'Upper Leg': 10,
  'Lower Leg': 11,
  'Feet': 12,
}

StatIndices = {
  'Health':0,
  'Stamina':1,
  'Oxygen':3,
  'Food':4,
  'Water':5,
  'Weight':7,
  'Melee Damage':8,
  'Movement Speed':9,
  'Fortitude':10,
  'Crafting Speed':11,
}

BodyColorIndices = {
  'Skin': 0,
  'Hair': 1,
  'Eye': 2,
}

def read_variable_data(stream):
  pair = stream.read_pair()
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
      'strings':
        [
          'PrimalCharacterSetting',
          'PrimalCharacterSetting_%s' % int(random.random() * 10),
          'SpawnUI_C_0',
          'ShooterGameInstance_0',
          'ShooterEngine_0',
        ]
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
      preset.header['strings'] = []

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
      stream.read_pair()
      struct_property_size = stream.readInt64()
      stream.readNullTerminatedString()
      while True:
        data = read_variable_data(stream)
        if data[0] is not None:
          preset.character_setting[data[0]] = data[1]
        else:
          break
      # End of Structured Data ---------------------------

    return preset

  def save_to_file(self, file_path):
    with open(file_path, 'wb') as ofile:
      stream = BinaryStream(ofile)
      # Start of Header ----------------------------------
      stream.writeChar(1)
      stream.writeBytesWith(19, 0)
      stream.writeNullTerminatedString(self.header['strings'][0])
      stream.writeInt32(1)
      stream.writeInt32(4)
      for i in xrange(1, len(self.header['strings'])):
        stream.writeNullTerminatedString(self.header['strings'][i])
      stream.writeBytesWith(12, 0)
      stream.writeInt64(166)
      # End of Header ------------------------------------

      # Start of Structured Data -------------------------
      slider_names = [
        'BodyColorSliderValue',
        'HairColorSliderValue',
        'EyeColorSliderValue',
        'BoneModifierSliderValues'
      ]
      struct_size = 174
      if self.character_setting['BodyColorSliderValue'] != 0.0:
        struct_size += 55
      if self.character_setting['HairColorSliderValue'] != 0.0:
        struct_size += 55
      if self.character_setting['EyeColorSliderValue'] != 0.0:
        struct_size += 54

      stream.writeNullTerminatedString('CharacterSetting')
      stream.writeNullTerminatedString('StructProperty')
      stream.writeInt64(struct_size)
      stream.writeNullTerminatedString('CharacterPreset')

      for name in slider_names:
        if self.character_setting[name] != 0.0:
          stream.writeNullTerminatedString(name)
          if name != slider_names[3]:
            stream.writeNullTerminatedString('FloatProperty')
            stream.writeInt64(4)
            stream.writeFloat(self.character_setting[name])
          else:
            stream.writeNullTerminatedString('ArrayProperty')
            stream.writeInt64(92)
            stream.writeNullTerminatedString('FloatProperty')
            length = len(self.character_setting[name])
            stream.writeInt32(length)
            for f in self.character_setting[name]:
              stream.writeFloat(f)

      stream.writeNullTerminatedString('None')
      stream.writeNullTerminatedString('None')
      stream.writeInt32(0)
      # End of Structured Data ---------------------------


class ArkProfile:
  """
  Responsible for loading and creating .arkprofile files
  At this moment, this class will not load the
  PlayerLocalData.arkprofile as that doesnt seem to follow the
  same structure as LocalPlayer.arkprofile and SteamID.arkprofile
  files do.

  ArkProfiles describe individual characters, their visual
  appearance, and some persistent data about them like Experience,
  Levels, and Engrams.
  """
  def __init__(self, file_path=None):
    self.data = {}
    if file_path is not None:
      with open(file_path, 'rb') as ifile:
        stream = BinaryStream(ifile)
        stream.readBytes(4)
        version = stream.readInt32()
        if version == 1:
          # Start of Header --------------------------
          stream.readBytes(16)
          print stream.readNullTerminatedString()
          stream.readBytes(8)
          print stream.readNullTerminatedString()
          print stream.readNullTerminatedString()
          print stream.readNullTerminatedString()
          print stream.readNullTerminatedString()
          print stream.readNullTerminatedString()
          stream.readBytes(20)
          # End of Header ----------------------------
          print '----------------------------------'
          var_name, var_type = stream.read_pair()
          print var_name, var_type
          if var_type == 'StructProperty':
            # print 'Struct Property found'
            struct = arktypes.load_struct(stream)
            # print struct.size

            self.data[var_name] = (var_type, struct)
            # self.data = struct
          print self.data
          # Only a null-terminated "None" and 4 NULL bytes remaining
        else:
          print 'Can\'t read PlayerLocalData.arkprofile types'
    self.myData = self.data['MyData'][1]

  def save_to_file(self, file_path):
    pass

  # API for Using the Data
  def get_exp(self):
    p_stats = self.myData.get('MyPersistentCharacterStats')
    return p_stats.get_exp()

  def set_exp(self, val):
    p_stats = self.myData.get('MyPersistentCharacterStats')
    fval = float(val)
    return p_stats.set_exp(val=fval)

  def add_exp(self, increment):
    exp = self.get_exp()
    new_val = exp + increment
    return self.set_exp(val=new_val)