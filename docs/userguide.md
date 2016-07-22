# Installation

```
pip install arkgamepy
```

- - -

# Getting Started

This section will help you get started using arkpy, by walking through some of the features provided by the library in a series of examples. If you're looking for API specific documentation check out the API Docs section.


## Reading an .arkprofile File

Start by importing the ark module from the arkpy package
```python
>>> from arkpy import ark
```

Now let's try reading an arkprofile stored in our SavedArksLocal directory
```python
>>> file_path = 'data/SavedArksLocal/LocalPlayer.arkprofile'
>>> profile = ark.ArkProfile(file_path)
>>> print profile
# <arkpy.ark.ArkProfile instance at 0x7f19767893f8>
```

Now that we've got an instance of ArkProfile we can start accessing some of the data, like the Character information.
```python
>>> print 'Name: %s' % profile.character.name.value
# Name: Woobles
>>> print 'Level: %s' % (profile.character.level_ups.value + 1)
# Level: 1
>>> print 'Sex: %s' % ('Female' if profile.character.isFemale.value else 'Male')
# Sex: Male
```

You'll see when we accessed the data belonging to character.name we did so with the **.value** property. This is because all the data parsed from the ark files are parsed as wrappers around the Data Types rather than the python Data Types themselves.

If we were to just character.name itself we'd get the following.
```python
>>> print profile.character.name
# <StrProperty> Woobles
```

## Editing an .arkprofile file

When we want to change the data, we can do so with the **.set()** method instead of **.value**.

```python
>>> profile.character.name.set('Spartacus')
>>> print 'I am %s!' % profile.character.name.value
# I am Spartacus!
```

Let's try leveling our character up.

```python
>>> profile.character.level_ups.set(9)
>>> profile.character.experience.set(450)
>>> print 'Level: %s' % (profile.character.level_ups.value + 1)
# Level: 10
```

**Important:** Arkpy is just a library for reading and writing the data, it doesn't provide (yet) any support for making sure you put in the right data. In the previous example we need to apply the appropriate amount of experience for the levels. Modded servers may also change the experience needed per level, so it's best if you check to see what those rates are first.

What good is leveling up if you don't spend any stat points?
```python
>>> print profile.character.stat_points
# [<ByteProperty> 0,
#  <ByteProperty> 0,
#  <ByteProperty> 0,
#  <ByteProperty> 0,
#  <ByteProperty> 0,
#  <ByteProperty> 0,
#  <ByteProperty> 0,
#  <ByteProperty> 0,
#  <ByteProperty> 0,
#  <ByteProperty> 0,
#  <ByteProperty> 0,
#  <ByteProperty> 0]
```

What is that? Well, those are all of our stats, currently at 0. You can set these stats by index if you know which stat corresponds to which index.

```python
>>> profile.character.stat_points[0].set(9)
>>> print profile.character.stat_points[0]
# <ByteProperty> 9
```

## Using Enums for Index-Based Values

If you don't know the index for the value you wish to manipulate, then you can use the Enums provided by Arkpy. Let's go back to the stat point example and use an Enum instead.


```python
>>> from arkpy.ark import StatMap
>>> profile.character.stat_points[StatMap.Health].set(5)
>>> profile.character.stat_points[StatMap.Weight].set(4)
```

You can also enumerate through the stats and display their values using the Enum:

```python
>>> stats = profile.character.stat_points
>>> for stat in StatMap:
>>>     print '%s: %s' % (stat.name, stats[stat].value)
# Health: 5
# Stamina: 0
# Oxygen: 0
# Food: 0
# Water: 0
# Weight: 4
# Melee_Damage: 0
# Movement_Speed: 0
# Fortitude: 0
# Crafting_Speed: 0
```

Maybe our character needs an engram or two now that he's leveled up.
```python
>>> campfire_path = 'BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Campfire.PrimalItemStructure_Campfire_C'
>>> campfire = ark.arktypes.ObjectProperty(campfire_path)
>>> profile.character.engrams.value.append(campfire)
>>> print profile.character.engrams
```

Because the engrams property on the character is an ArrayProperty[ObjectProperty] there's a lot of text that goes in to adding just a single engram. Especially important is the Entity Path for the engram. An easier way to do this is to use the Object Entity Path Two-Way Dictionaries.

## Using Object Entity Path Two-Way Dictionary

This dictionary is especially helpful for converting a simple description of an item or engram like 'Campfire' to a path that looks like: 'BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints...' and vice-versa.

Coming Soon.