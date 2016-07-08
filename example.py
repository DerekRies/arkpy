import random

from arkpy import arktypes
from arkpy.ark import ArkCharacterSetting, ArkProfile



def load_arkprofile():
  # fp = 'data/SavedArksLocal/LocalPlayer.arkprofile'
  # fp = 'data/TheCenterSavedArksLocal/LocalPlayer.arkprofile'
  fp = 'data/76561197972327357.arkprofile'
  # fp = 'data/LocalProfiles/PlayerLocalData.arkprofile'
  profile = ArkProfile(fp)

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

  # c = arktypes.PrimalPlayerDataStruct()
  # print c.size
  load_arkprofile()


  # character = ArkCharacterSetting()
  # character.character_setting['BodyColorSliderValue'] = random.random()
  # character.character_setting['EyeColorSliderValue'] = random.random()
  # bone_sliders = character.character_setting['BoneModifierSliderValues']
  # l = len(bone_sliders)
  # for i in xrange(l):
  #   bone_sliders[i] = random.random()
  # character.save_to_file(fp)


if __name__ == '__main__':
  main()