ARKpy
====

**v0.0**

ARKpy is a library for reading and writing the file formats of ARK: Survival Evolved with the python programming language. ARKpy does not simply look for the offsets of particular strings to find the data (like other existing libraries/scripts), but reads the entire data structure of the file into memory.

For those interested in the reverse engineering of the file types the specifications can be found among the library docs.

[Docs](http://arkpy.readthedocs.io/en/latest/) **|**
[File Format Specs](http://arkpy.readthedocs.io/en/latest/formats/)


## Features
 - Read and Write the following file types
    - **.arkcharactersetting** (Character creator preset files)
    - **.arkprofile** (LocalPlayer.arkprofile or steamid.arkprofile, no LocalPlayerData)
    - **.arktribe**
 - Create new characters or tribes dynamically
 - Friendly API wrapper around the data
 - Maps to enumerate through and identify the proper index for:
    - **BoneModifierSlots** (Head Size, Chest, etc...)
    - **Body Colors** (Skin, Hair, Eyes)
    - **Stats** (Health, Oxygen, Stamina, etc...)
    - **Item Blueprint Paths/IDs**


## Usage

#### Reading an .arkprofile file
```python
from arkpy.ark import ArkProfile
from arkpy.ark import BoneMap, StatMap, BodyColorMap

file_path = 'data/SavedArksLocal/LocalPlayer.arkprofile'
profile = ArkProfile(file_path)

print profile.character.name
print profile.character.level_ups
print profile.character.experience
print profile.character.engram_points

# Get all the Stat points allocated and print them with a string
# identifying which stat they are
stats = profile.character.stat_points
for stat in StatMap:
  print '%s: %s' % (stat.name, stats[stat])

# Get all the BoneModifier values and print them with a string
# identifying which bone it is
bones = profile.character.body_modifiers
for bone in BoneMap:
  print '%s: %s' % (bone.name, bones[bone])
```

## Installation
Soon to be hosted on Pypi.