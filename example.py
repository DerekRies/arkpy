import random

from arkpy import arktypes
from arkpy.ark import ArkCharacterSetting, ArkProfile
from arkpy.ark import BoneMap, StatMap, BodyColorMap



def load_arkprofile():
  # fp = 'data/SavedArksLocal/LocalPlayer.arkprofile'
  # fp = 'data/TheCenterSavedArksLocal/LocalPlayer.arkprofile'
  # fp = 'data/76561197972327357.arkprofile'
  # fp = 'data/LocalPlayerRosetta.arkprofile'
  # fp = 'data/LocalProfiles/PlayerLocalData.arkprofile'
  # fp = 'data/1242116633.arktribe'
  fp = 'data/testoutput.arkprofile'
  profile = ArkProfile(fp)
  # profile.character.set_name('Hammy')
  # print profile.character.get_name()
  # profile.character.name.set('Hammy')
  print profile.character.name
  print profile.character.body_colors
  bones = profile.character.bone_modifiers

  print 'engrams------------------'
  print len(profile.character.engrams.value)

  # for engram in profile.character.engrams.value:
    # print engram.value

  # profile.character.add_engram('Campfire')
  # print len(profile.character.engrams.value)
  # print engrams.value
  # print profile.myData.data['AppIDSet'].value
  # print profile.character.default_slots
  # print profile.character.default_slots[0].value
  # for bone in BoneMap:
  #   print '%s: %s' % (bone.name, bones[bone])
  # stats = profile.character.stat_points
  # for stat in StatMap:
  #   print '%s: %s' % (stat.name, stats[stat])

def create_profile():
  profile = ArkProfile()
  profile.player_name.set('Teflon Don')
  profile.character.name.set('Boggsy')
  print profile.character.name
  profile.character.bone_modifiers[BoneMap.Chest].set(1.0)
  profile.character.bone_modifiers[BoneMap.Shoulders].set(0.333)
  print profile.character.engrams.value.append(arktypes.ObjectProperty('Campfire'))
  # print profile.myData.data
  # print profile.character._config.data
  # print profile.character._stats.data
  # for key in profile.myData.data:
    # print key
  profile.save_to_file('data/testoutput.arkprofile')

def main():
  # fp = 'data/SavedArksLocal/min.arkcharactersetting'
  # fp = 'data/SavedArksLocal/minandblack.arkcharactersetting'
  # fp = 'data/SavedArksLocal/maxandbrown.arkcharactersetting'
  # fp = 'data/SavedArksLocal/mini.arkcharactersetting'
  # fp = 'data/SavedArksLocal/defaultmale.arkcharactersetting'
  # fp = 'data/throwaway.arkcharactersetting'
  # fp = 'data/random.arkcharactersetting'
  # character = ArkCharacterSetting.from_file(fp)
  # print character.character_setting

  # character = ArkCharacterSetting()
  # character.character_setting['BodyColorSliderValue'] = random.random()
  # character.character_setting['EyeColorSliderValue'] = random.random()
  # bone_sliders = character.character_setting['BoneModifierSliderValues']
  # l = len(bone_sliders)
  # for i in xrange(l):
  #   bone_sliders[i] = random.random()
  # character.save_to_file(fp)

  # load_arkprofile()
  create_profile()

if __name__ == '__main__':
  main()