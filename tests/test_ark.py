import pytest
import random
import os

from context import arktypes, ark, binary


data_dir = 'data/'
output_dir = 'tests/output/'


class TestArkProfile:
  def test_write_read(self):
    profile = ark.ArkProfile()
    profile.map_name = ark.GameMapMap.the_center
    profile.map_path = ark.GameMapMap.the_center_path
    profile.unique_id.set('11111111111111111')
    profile.player_name.set('Fake Steam Name')
    profile.player_id.set(ark._gen_player_id())
    profile.first_spawned.set(True)
    profile.character.name.set('GeneratedCharacter')
    profile.character.level_ups.set(9)
    profile.character.experience.set(450)
    profile.character.stat_points[ark.StatMap.Health].set(9)
    profile.save_to_file(output_dir + 'generatedprofile.arkprofile')

    # TODO: Create some functionality to compare the data dicts directly
    # to see if they are the same
    profile2 = ark.ArkProfile(output_dir + 'generatedprofile.arkprofile')
    assert profile2.map_name == profile.map_name
    assert profile2.map_path == profile.map_path
    assert profile2.unique_id.value == profile.unique_id.value
    assert profile2.player_name.value == profile.player_name.value
    assert profile2.player_id.value == profile.player_id.value
    assert profile2.character.isFemale.value == profile.character.isFemale.value
    assert profile2.character.stat_points[ark.StatMap.Health].value == 9


class TestArkTribe:
  def test_write_read(self):
    owner_id = ark._gen_player_id()
    owner_name = arktypes.StrProperty(value='Generated Owner')
    tribe = ark.ArkTribe()
    tribe.name.set('Generated Tribe')
    tribe.tribe_id.set(ark._gen_tribe_id())
    tribe.owner_id.set(owner_id)
    tribe.members_names.value.append(owner_name)
    member_id = arktypes.UInt32Property(value=owner_id)
    tribe.members_ids.value.append(member_id)
    tribe.save_to_file(output_dir + 'generatedtribe.arktribe')

    tribe2 = ark.ArkTribe(output_dir + 'generatedtribe.arktribe')
    assert tribe2.name.value == tribe.name.value
    assert tribe2.tribe_id.value == tribe.tribe_id.value
    assert tribe2.members_names.value[0].value == tribe.members_names.value[0].value
    assert tribe2.owner_id.value == tribe.owner_id.value


@pytest.mark.slow
class TestBulkReads:
  def test_read_profiles(self):
    path = 'data/Servers/Server01/'
    files = os.listdir(path)
    for file in files:
      if '.arkprofile' in file:
        try:
          file_path = path + file
          profile = ark.ArkProfile(file_path)
        except:
          print 'FAILED: %s' % file
  def test_read_tribes(self):
    assert True