# `arkpy.ark` Module

## `Character` Class

Character is a higher-level wrapper around the PrimalPlayerConfigStruct andPrimalPersistentCharacterStatsStruct, that exposes all of their properties hidden amongst their .data dictionary as easier and shorter properties.

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

Description

### **Properties**
### **Methods**

- - -

## `ArkTribe` Class

Description

### **Properties**
### **Methods**

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

## `GameMapMap` Class

`GameMapMap` is a mapping of the map names and map paths to the appropriate index values they can be found in.

| Name       | Value |
|------------|-------|
| **the_island** | 'TheIsland' |
| **the_island_path** | '/Game/Maps/TheIslandSubMaps/TheIsland' |
| **the_center** | 'TheCenter' |
| **the_center_path** | '/Game/Mods/TheCenter/TheCenter' |

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