import random

from arkpy import arktypes
from arkpy.ark import ArkCharacterSetting, ArkProfile



def load_arkprofile():
  # fp = 'data/SavedArksLocal/LocalPlayer.arkprofile'
  # fp = 'data/TheCenterSavedArksLocal/LocalPlayer.arkprofile'
  # fp = 'data/76561197972327357.arkprofile'
  fp = 'data/LocalPlayerRosetta.arkprofile'
  # fp = 'data/LocalProfiles/PlayerLocalData.arkprofile'
  # fp = 'data/1242116633.arktribe'
  profile = ArkProfile(fp)
  profile.character.set_name('Hammy')
  print profile.character.get_name()
  print profile.character.get_body_color(0)

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

  load_arkprofile()

if __name__ == '__main__':
  main()