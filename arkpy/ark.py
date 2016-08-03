"""
Collection of file readers and writers for some of the Ark: Survival Evolved
file types.
"""

import random
import utils
import arktypes
import warnings

from binary import BinaryStream
from enum import IntEnum


class WrongFileType(Exception):
    pass


class GameMapMap:
    the_island = 'TheIsland'
    the_island_path = '/Game/Maps/TheIslandSubMaps/TheIsland'
    the_center = 'TheCenter'
    the_center_path = '/Game/Mods/TheCenter/TheCenter'


class BoneMap(IntEnum):
    Head_Size = 0
    Upper_Face_Size = 15
    Lower_Face_Size = 16
    Head_Width = 19
    Head_Height = 18
    Head_Depth = 20
    Hand = 8
    Arm_Length = 5
    Upper_Arm = 6
    Lower_Arm = 7
    Neck_Size = 1
    Neck_Length = 2
    Chest = 3
    Shoulders = 4
    Hip = 13
    Torso_Width = 14
    Torso_Height = 21
    Torso_Depth = 17
    Leg_Length = 9
    Upper_Leg = 10
    Lower_Leg = 11
    Feet = 12


class StatMap(IntEnum):
    Health = 0
    Stamina = 1
    Oxygen = 3
    Food = 4
    Water = 5
    Weight = 7
    Melee_Damage = 8
    Movement_Speed = 9
    Fortitude = 10
    Crafting_Speed = 11


class BodyColorMap(IntEnum):
    Skin = 0
    Hair = 1
    Eye = 2


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


class Character:

    """
    API Wrapper around the PersistentCharacterStats and
    CharacterConfig structs that will be used by FileReaders
    that share these structs in common, like .arkprofile and
    .arktribe files.
    """

    def __init__(self, stats=None, config=None):
        if stats is None and config is None:
            msg = 'You probably want to create an ArkProfile instead.'
            warnings.warn(msg)
        self._stats = stats
        self._config = config

    @property
    def name(self):
        return self._config.data['PlayerCharacterName']

    @property
    def isFemale(self):
        return self._config.data['bIsFemale']

    @property
    def body_colors(self):
        return self._config.data['BodyColors']

    @property
    def bone_modifiers(self):
        return self._config.data['RawBoneModifiers']

    @property
    def spawn_region(self):
        return self._config.data['PlayerSpawnRegionIndex']

    @property
    def experience(self):
        return self._stats.data['CharacterStatusComponent_ExperiencePoints']

    @property
    def level_ups(self):
        s = 'CharacterStatusComponent_ExtraCharacterLevel'
        ecl = self._stats.data[s]
        return ecl

    @property
    def stat_points(self):
        s = 'CharacterStatusComponent_NumberOfLevelUpPointsApplied'
        return self._stats.data[s]

    @property
    def engram_points(self):
        return self._stats.data['PlayerState_TotalEngramPoints']

    @property
    def engrams(self):
        return self._stats.data['PlayerState_EngramBlueprints']

    def add_engram(self, item):
        self.engrams.value.append(item)
        self.engrams.length = len(self.engrams.value)
        # Each item added to ArrayProperty<ObjectProperty> for engrams
        # 4 Bytes for Prefix (01 00 00 00)
        # N Bytes for NTString (Int32, String, NULL)
        item_size = 9 + len(item)
        self.engrams.size = self.engrams.size + item_size

    @property
    def default_slots(self):
        return self._stats.data['PlayerState_DefaultItemSlotClasses']


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
            strings = preset.header['strings']
            strings.append(stream.readNullTerminatedString())
            stream.readBytes(4)
            # Guessing that this `04 00 00 00` refers to how many strings are
            # to follow. If not, then these bytes are unknown and there are
            # just 4 strings following regardless
            for i in xrange(stream.readInt32()):
                strings.append(stream.readNullTerminatedString())
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
        self.file_type = 'PrimalPlayerData'
        self.name = 'PrimalPlayerData_%s' % 0
        self.game_mode = 'PersistentLevel'
        self.map_name = 'TheIsland'
        self.map_path = '/Game/Maps/TheIslandSubMaps/TheIsland'
        if file_path is not None:
            with open(file_path, 'rb') as ifile:
                stream = BinaryStream(ifile)
                stream.readBytes(4)
                version = stream.readInt32()
                if version == 1:
                    # Start of Header --------------------------
                    stream.readBytes(16)
                    self.file_type = stream.readNullTerminatedString()
                    stream.readBytes(8)
                    self.name = stream.readNullTerminatedString()
                    stream.readNullTerminatedString()
                    self.game_mode = stream.readNullTerminatedString()
                    self.map_name = stream.readNullTerminatedString()
                    self.map_path = stream.readNullTerminatedString()
                    stream.readBytes(12)
                    self.header_size = stream.readInt32()
                    stream.readInt32()
                    # End of Header ----------------------------
                    # print '----------------------------------'
                    var_name, var_type = stream.read_pair()
                    # print var_name, var_type
                    if var_type == 'StructProperty':
                        # print 'Struct Property found'
                        struct = arktypes.load_struct(stream)
                        # print struct.size
                        struct.var_name = var_name

                        self.data[var_name] = struct
                        # self.data = struct
                    # print self.data
                    # Only a null-terminated "None" + 4 NULL bytes remaining
                else:
                    raise WrongFileType(
                        "PlayerLocalData.arkprofile files unsupported")
        self.myData = self.data.get(
            'MyData', arktypes.PrimalPlayerDataStruct())
        statsstruct = self.myData.get('MyPersistentCharacterStats')
        configstruct = self.myData.get('MyPlayerCharacterConfig')
        self.character = Character(stats=statsstruct, config=configstruct)

    @property
    def player_id(self):
        return self.myData.data['PlayerDataID']

    @property
    def unique_id(self):
        return self.myData.data['UniqueID']

    @property
    def network_address(self):
        return self.myData.data['SavedNetworkAddress']

    @property
    def player_name(self):
        return self.myData.data['PlayerName']

    @property
    def first_spawned(self):
        return self.myData.data['bFirstSpawned']

    @property
    def is_spectator(self):
        return self.myData.data['bIsSpectator']

    @property
    def tribe_ID(self):
        return self.myData.data['TribeID']

    @property
    def player_version(self):
        return self.myData.data['PlayerDataVersion']

    def _write_header_to_stream(self, stream):
        stream.writeInt32(1)
        stream.writeInt32(1)
        stream.writeBytesWith(16, 0)
        stream.writeNullTerminatedString(self.file_type)
        stream.writeInt32(0)
        stream.writeInt32(5)
        stream.writeNullTerminatedString(self.name)
        stream.writeNullTerminatedString('ArkGameMode')
        stream.writeNullTerminatedString(self.game_mode)
        stream.writeNullTerminatedString(self.map_name)
        stream.writeNullTerminatedString(self.map_path)
        stream.writeBytesWith(12, 0)
        self.header_size = stream.tell() + 8
        stream.writeInt32(self.header_size)
        stream.writeInt32(0)

    def save_to_file(self, file_path):
        with open(file_path, 'wb') as ofile:
            stream = BinaryStream(ofile)
            self._write_header_to_stream(stream)
            # Struct will call each prop and child structs write methods
            self.myData._write_to_stream(stream)
            stream.writeNullTerminatedString('None')
            stream.writeInt32(0)


class ArkTribe:

    def __init__(self, file_path=None):
        self.data = {}
        self.file_type = 'PrimalTribeData'
        self.number = 0
        self.game_mode = 'PersistentLevel'
        self.map_name = 'TheIsland'
        self.map_path = '/Game/Maps/TheIslandSubMaps/TheIsland'
        self.version = 1
        if file_path is not None:
            self._load_from_stream(file_path)
        self.container = self.data.get('TribeData', arktypes.TribeData())

    def _load_from_stream(self, file_path):
        with open(file_path, 'rb') as ifile:
            stream = BinaryStream(ifile)
            stream.readBytes(24)
            self.file_type = stream.readNullTerminatedString()
            stream.readBytes(8)
            self.number = stream.readNullTerminatedString().split('_')[1]
            self.number = int(self.number)
            stream.readNullTerminatedString()
            self.game_mode = stream.readNullTerminatedString()
            self.map_name = stream.readNullTerminatedString()
            self.map_path = stream.readNullTerminatedString()
            stream.readBytes(20)
            var_name, var_type = stream.read_pair()
            print var_name
            print var_type
            struct = arktypes.load_struct(stream)
            struct.var_name = var_name
            self.data[var_name] = struct

    def _write_header_to_stream(self, stream):
        stream.writeInt32(1)
        stream.writeInt32(1)
        stream.writeBytesWith(16, 0)
        stream.writeNullTerminatedString(self.file_type)
        stream.writeInt32(0)
        stream.writeInt32(5)
        data_number_str = '%s_%s' % (self.file_type, self.number)
        stream.writeNullTerminatedString(data_number_str)
        stream.writeNullTerminatedString('ArkGameMode')
        stream.writeNullTerminatedString(self.game_mode)
        stream.writeNullTerminatedString(self.map_name)
        stream.writeNullTerminatedString(self.map_path)
        stream.writeBytesWith(12, 0)
        header_size = stream.tell() + 8
        stream.writeInt32(header_size)
        stream.writeInt32(0)

    def save_to_file(self, file_path):
        with open(file_path, 'wb') as ofile:
            stream = BinaryStream(ofile)
            self._write_header_to_stream(stream)
            self.container._write_to_stream(stream)
            stream.writeNullTerminatedString('None')
            stream.writeInt32(0)

    @property
    def name(self):
        return self.container.data['TribeName']

    @property
    def owner_id(self):
        return self.container.data['OwnerPlayerDataID']

    @property
    def tribe_id(self):
        return self.container.data['TribeID']

    @property
    def members_names(self):
        return self.container.data['MembersPlayerName']

    @property
    def members_ids(self):
        return self.container.data['MembersPlayerDataID']

    @property
    def members_ranks(self):
        return self.container.data['MembersRankGroups']

    @property
    def members(self):
        return zip(self.members_names.value, self.members_ids.value)

    @property
    def government_set(self):
        return self.container.data['bSetGovernment']

    @property
    def tribe_admins(self):
        return self.container.data['TribeAdmins']

    @property
    def alliances(self):
        return self.container.data['TribeAlliances']

    @property
    def government(self):
        return self.container.data['TribeGovernment']

    @property
    def member_configs(self):
        return self.container.data['MemberConfigs']

    @property
    def log(self):
        return self.container.data['TribeLog']

    @property
    def log_index(self):
        return self.container.data['LogIndex']
