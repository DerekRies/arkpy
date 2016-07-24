# `arkpy.ark` Module

This is the primary user-facing module defined by the `arkpy` package. While the `arktypes` module is primarily concerned with the low-level reading/writing of the file types, this module provides the developer interface for reading that data and creating new files.

- - -

## `Character` Class

Character is a higher-level wrapper around the `PrimalPlayerConfigStruct` and `andPrimalPersistentCharacterStatsStruct`, that exposes all of their properties hidden amongst their .data dictionary as easier and shorter properties.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **name** | `StrProperty` | A Character's name (not the steam name) |
| **isFemale** | `BoolProperty` | Flag specifying whether or not the character is female |
| **body_colors** | `list[LinearColor]` | A python list of `LinearColor`s indexed according to the `BodyColorMap` |
| **bone_modifiers** | `list[FloatProperty]` | A python list of bone values (0.0-1.0) to configure the characters appearance, indexed according to `BoneMap` |
| **spawn_region** | `IntProperty` | The region of the map this character spawned from. An integer from 0-9 |
| **experience** | `FloatProperty` | The experience that this character has gained |
| **level_ups** | `UInt16Property` | The number of times a character has leveled up. This is the character's level - 1. |
| **stat_points** | `list[ByteProperty]` | A python list of `ByteProperty`, indexed according to `StatMap`, where each value is the number of times that stat has been leveled up |
| **engram_points** | `IntProperty` | The number of engram points that this character has available to them, not the total amount they've earned. |
| **engrams** | `ArrayProperty[ObjectProperty]` | An ArrayProperty of ObjectPropertys where each item is an Object Entity Path for the engrams that have been learned |
| **default_slots** | `list[ObjectProperty]` | A python list of ObjectPropertys where each item is indexed by it's slot position, and the ObjectProperty is an Object Entity Path for an item/engram |

### **Methods**

- - -

## `ArkProfile` Class

Responsible for loading and creating .arkprofile files. At this moment, this class will not load the PlayerLocalData.arkprofile as that doesnt seem to follow the same structure as LocalPlayer.arkprofile and SteamID.arkprofile files do.

ArkProfiles describe individual characters, their visual appearance, and some persistent data about them like Experience, Levels, and Engrams.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **data** | `dict`| The raw data loaded from an .arkprofile file as a tree-like structure. It is recommended you use the properties provided by `ArkProfile` and `Character` instead of drilling into **data** |
| **file_type** | `str`| Always **'PrimalPlayerData'** |
| **name** | `str`| **'PrimalPlayerData_'** appended with the number of this file |
| **game_mode** | `str`| Always **'PersistentLevel'** |
| **map_name** | `str`| Name of the map this character is on, 'TheIsland' or 'TheCenter' |
| **map_path** | `str`| Path to the map, looks like '/Game/Maps/TheIslandSubMaps/TheIsland'. Can use the `GameMapMap` to reference these paths easier. |
| **character** | `Character`| Wrapper around the low-level structs for character information. Recommended to use this rather than digging into the data dict |
| **player_id** | `UInt64Property`| |
| **player_name** | `StrProperty`| Player's steam name they used when they first created this character. This value is not updated if they change their steam name |
| **unique_id** | `UniqueNetIdRepl`| |
| **network_address** | `StrProperty`| |
| **first_spawned** | `BoolProperty`| True when the character has spawned for the first time |
| **tribe_ID** | `IntProperty`| The ID belonging to the Tribe this player is in. Tribe ID can be used to fetch tribe data by looking for a tribeID.arktribe file |
| **player_version** | `IntProperty`| Always 1 |


### **Methods**

**ArkProfile**(file_path=None)

Constructor method for creating an ArkProfile. Can be created programmatically or loaded from a file by specifying the **file_path**

| Parameter Name | Type | Description |
|------|------|-------------|
|**file_path** | `str`  | Path to an .arkprofile file that will be loaded into this ArkProfile with it's data |

  - **returns** a new `ArkProfile`


**save_to_file(file_path)**

Saves this ArkProfile to an .arkprofile file named **file_path**

| Parameter Name | Type | Description |
|------|------|-------------|
|**file_path**| `str` | The file path that this .arkprofile file will be saved to |

  - **returns:** `None`

**_write_header_to_stream(stream)**

**(Internal)** Writes all the header information to the `BinaryStream` specified.

| Parameter Name | Type | Description |
|------|------|-------------|
|**stream**| `BinaryStream` | A Binary stream that this StrProperty can build itself from |

  - **returns:** `None`


- - -

## `ArkTribe` Class

Responsible for loading and creating .arktribe files. ArkTribes describe individual tribes, their members, alliances, government structure, and even a log of events that happen to the Tribe.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **data** | `dict`| The raw data loaded from an .arkprofile file as a tree-like structure. It is recommended you use the properties provided by `ArkTribe` and `Character` instead of drilling into **data** |
| **file_type** | `str`| Always **'PrimalTribeData'** |
| **number** | `int`| The number after 'PrimalTribeData_' in the file, which is probably just an incrementing integer for each file that's created. |
| **game_mode** | `str`| Always **'PersistentLevel'** |
| **map_name** | `str`| Name of the map this character is on, 'TheIsland' or 'TheCenter' |
| **map_path** | `str`| Path to the map, looks like '/Game/Maps/TheIslandSubMaps/TheIsland'. Can use the `GameMapMap` to reference these paths easier. |
| **version** | `int` | 1 for now |
| **name** | `str` | Tribe's name |
| **owner_id** | `str` | The PlayerID belonging to the owner of the tribe |
| **tribe_id** | `str` | Tribe's ID, same as file name |
| **members_names** | `ArrayProperty[]` | An ArrayProperty of the names belonging to all the members in the tribe |
| **members_ids** | `ArrayProperty[]` | An ArrayProperty of the IDs belonging to all the members in the tribe |
| **members** | `list[(str, int)]` | Convenience property, returns a list of member tuples. Each tuple has the members name and then the members ID. **NOTE:** the data in the tuple is the actual python data-type, not the Property wrapper. |
| **government_set** | `bool` | True when this Tribe has a government structure |
| **government** | `TribeGovernment` | `TribeGovernment` struct with the government configuration for this Tribe. |
| **tribe_admins** | `ArrayProperty[]` | An ArrayProperty of all the member IDs that are also admins |
| **alliances** | `ArrayProperty[]` | An ArrayProperty of all the alliances that this Tribe belongs to. Each item in the array is a `TribeAlliance` struct |
| **member_configs** | `ArrayProperty[]` | An ArrayProperty of the `PrimalPlayerConfigStruct`s belonging to members' characters. |
| **log** | `ArrayProperty[]` | An array of all the events added to the Tribe Log |
| **log_index** | `int` | Because the log stores a finite amount of events, the log index represents the current position in the unlimited log |

### **Methods**

**ArkTribe**(file_path=None)

Constructor method for creating an ArkTribe. Can be created programmatically or loaded from a file by specifying the **file_path**

| Parameter Name | Type | Description |
|------|------|-------------|
|**file_path** | `str`  | Path to an .arkTribe file that will be loaded into this ArkTribe with it's data |

  - **returns** a new `ArkTribe`



- - -

## `BoneMap` Class
### extends `IntEnum`

`BoneMap` is a mapping of the bone names for character configuration to the appropriate index values they can be found in.

| Name | Value |
|------|-------|
| **Head_Size** | 0 |
| **Upper_Face_Size** | 15 |
| **Lower_Face_Size** | 16 |
| **Head_Width** | 19 |
| **Head_Height** | 18 |
| **Head_Depth** | 20 |
| **Hand** | 8 |
| **Arm_Length** | 5 |
| **Upper_Arm** | 6 |
| **Lower_Arm** | 7 |
| **Neck_Size** | 1 |
| **Neck_Length** | 2 |
| **Chest** | 3 |
| **Shoulders** | 4 |
| **Hip** | 13 |
| **Torso_Width** | 14 |
| **Torso_Height** | 21 |
| **Torso_Depth** | 17 |
| **Leg_Length** | 9 |
| **Upper_Leg** | 10 |
| **Lower_Leg** | 11 |
| **Feet** | 12 |


- - -

## `BodyColorMap` Class
### extends `IntEnum`

`BodyColorMap` is a mapping of readable body color regions, to the index values used by the game to represent them

| Name       | Value |
|------------|-------|
| **Skin** | 0 |
| **Hair** | 1 |
| **Eye** | 2 |

- - -

## `StatMap` Class
### extends `IntEnum`

`StatMap` is a mapping of the stat names for character stats to the appropriate index values they can be found in.

| Name   | Value |
|--------|---|
| **Health** | 0 |
| **Stamina** | 1 |
| **Oxygen** | 3 |
| **Food** |  4 |
| **Water** | 5 |
| **Weight** | 7 |
| **Melee_Damage** | 8 |
| **Movement_Speed** | 9 |
| **Fortitude** | 10 |
| **Crafting_Speed** | 11 |

- - -

## `GameMapMap` Class

`GameMapMap` is a mapping of the map names and map paths to the appropriate index values they can be found in.

| Name       | Value |
|------------|-------|
| **the_island** | 'TheIsland' |
| **the_island_path** | '/Game/Maps/TheIslandSubMaps/TheIsland' |
| **the_center** | 'TheCenter' |
| **the_center_path** | '/Game/Mods/TheCenter/TheCenter' |
