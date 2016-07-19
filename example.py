import random

from arkpy import arktypes
from arkpy.ark import ArkCharacterSetting, ArkProfile, ArkTribe
from arkpy.ark import BoneMap, StatMap, BodyColorMap
from arkpy import utils


def load_arkprofile():
  # fp = 'data/SavedArksLocal/LocalPlayer.arkprofile'
  # fp = 'data/TheCenterSavedArksLocal/LocalPlayer.arkprofile'
  # fp = 'data/76561197972327357.arkprofile'
  # fp = 'data/LocalPlayerRosetta.arkprofile'
  # fp = 'data/LocalProfiles/PlayerLocalData.arkprofile'
  # fp = 'data/testoutput.arkprofile'
  fp = 'data/Servers/Server01/76561198006283537.arkprofile'
  profile = ArkProfile(fp)
  # profile.character.set_name('Hammy')
  # print profile.character.get_name()
  # profile.character.name.set('Hammy')
  print profile.player_name
  print profile.character.name
  print profile.character.level_ups.value + 1
  print 'Tribe: %s' % profile.data['MyData'].data['TribeID'].value
  # print profile.character.body_colors
  # bones = profile.character.bone_modifiers

  # print 'engrams------------------'
  print 'Engrams: %s' % len(profile.character.engrams.value)
  # for engram in profile.character.engrams.value:
    # print engram
  # for engram in profile.character.engrams.value:
    # print engram.value
  # for bone in BoneMap:
  #   print '%s: %s' % (bone.name, bones[bone])
  stats = profile.character.stat_points
  for stat in StatMap:
    print '%s: %s' % (stat.name, stats[stat])

  slots = profile.character.default_slots
  for slot in slots:
    print 'Slot: %s %sx' % (utils.get_item(slot.value), slot.quantity)



def create_profile():
  profile = ArkProfile()
  profile.player_name.set('Teflon Don')
  profile.character.name.set('Boggsy')
  print profile.character.name
  print profile.character.level_ups
  profile.character.bone_modifiers[BoneMap.Chest].set(1.0)
  profile.character.bone_modifiers[BoneMap.Shoulders].set(0.333)
  profile.character.stat_points[StatMap.Health].set(5)
  profile.character.stat_points[StatMap.Weight].set(15)
  profile.character.level_ups.set(5)
  profile.save_to_file('data/testoutput.arkprofile')

def load_arktribe():
  # fp = 'data/1242116633.arktribe'
  # fp = 'data/Servers/Server01/1020553874.arktribe'
  # fp = 'data/Servers/Server01/1060351590.arktribe'
  # fp = 'data/Servers/Server01/1040644402.arktribe'
  fp = 'data/Servers/Server01/1058612644.arktribe'
  # fp = 'data/1082816853.arktribe'
  tribe = ArkTribe(fp)
  # tribe = ArkTribe()
  # tribe.name.set('Genesis')
  # print tribe.name
  print 'Tribe Name: %s' % tribe.name.value
  # for entry in tribe.log.value:
    # print entry

  print 'Alliances'
  alliances = tribe.alliances
  if alliances is not None:
    for alliance in tribe.alliances.value:
      print 'Alliance Name: %s' % alliance.data['AllianceName'].value
      for t in alliance.data['MembersTribeName'].value:
        print '    Tribe Name: %s' % t.value
      print '-------------------------------------'


def create_tribe():
  tribe = ArkTribe()
  tribe.number = 21
  tribe.name.set('Genesis')
  tribe.tribe_id.set(929328)
  owner = {'mid': 1337, 'name': 'Mugu Man', 'admin': True}
  m1 = {'mid': 8008, 'name': 'Drone One', 'admin': False}
  m2 = {'mid': 6969, 'name': 'Drone Two', 'admin': False}
  m3 = {'mid': 9230, 'name': 'Officer Biggles', 'admin': True}
  members = [owner, m1, m2, m3]

  tribe.owner_id.set(owner['mid'])
  for newmember in members:
    mname = arktypes.StrProperty(newmember['name'])
    mid = arktypes.UInt32Property(newmember['mid'])
    tribe.members_names.value.append(mname)
    tribe.members_ids.value.append(mid)
    if newmember['admin']:
      tribe.tribe_admins.value.append(mid)

  print tribe.container.data
  print 'Tribe Name: %s' % tribe.name.value
  print 'Owner: %s' % tribe.owner_id.value
  print 'Members:'
  for mname, mid in tribe.members:
    print '  Name: %s | ID: %s' % (mname.value, mid.value)
  tribe.save_to_file('data/firstoutput.arktribe')


def read_and_write_tribe():
  fp = 'data/Servers/Server01/1058612644.arktribe'
  tribe = ArkTribe(fp)
  tribe.save_to_file('data/1058612644-resave.arktribe')


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
  # load_arktribe()
  # create_profile()
  # create_tribe()
  read_and_write_tribe()

if __name__ == '__main__':
  main()