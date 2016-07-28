!!! Note
    This part of the documentation is geared towards how to use the library for some of the more general tasks, as well as some information about the general structure of the data you'll be dealing with.

# Installation

```
pip install arkgamepy
```

!!! Note
    There is another package on PyPi named arkpy, do not install that one.


- - -

# Getting Started

This section will help you get started using arkpy, by walking through some of the features provided by the library in a series of examples. If you're looking for API specific documentation check out the [API Docs](arkmodule.md) section.


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

- - -

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

!!! Note
    Arkpy is just a library for reading and writing the data, it doesn't provide (yet) any support for making sure you put in the right data. In the previous example we need to apply the appropriate amount of experience for the levels. Modded servers may also change the experience needed per level, so it's best if you check to see what those rates are first.

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

- - -

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
>>> from arkpy import arktypes
>>> campfire_path = 'BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Items/Structures/Misc/PrimalItemStructure_Campfire.PrimalItemStructure_Campfire_C'
>>> campfire = ark.arktypes.ObjectProperty(campfire_path)
>>> profile.character.engrams.value.append(campfire)
>>> print profile.character.engrams
```

- - -

## Using the Entities Module

Because the engrams property on the character is an ArrayProperty[ObjectProperty] there's a lot of text that goes in to adding just a single engram. Especially important is the Entity Path for the engram. An easier way to do this is to use the `Enum`s in the [entities module](entities.md).

Let's redo the previous example and add the campfire engram to the character's learned engrams.

```python
from arkpy import arktypes, entities
campfire = arktypes.ObjectProperty(entities.Structure.Campfire.value)
profile.character.engrams.value.append(campfire)
```

- - -

## Saving a Character

Once we've completed all of our changes we can save the profile to an .arkprofile file by calling the `save_to_file()` method.

```python
# Recommended: don't overwrite the files you read in without backing them
# up as you may corrupt them in the process.
profile.save_to_file('data/SavedArksLocal/LocalPlayer.edit.arkprofile')
```


- - -

## Loading the Generated Character File

!!! Important
    Always keep backups of the files before you make any changes to them. Also don't remove the **.profilebak** files when you replace the **.arkprofile** files.

First, let's take a look at how Ark loads game files into memory.

- - -

### Ark Loading Process

1. Loads the world save, **.ark** file
2. Looks for a file named **LocalPlayer.arkprofile**, if not found, uses any other **.arkprofile** file it can find.
3. Copys contents of **LocalPlayer.arkprofile** into the **.profilebak** file.
4. On exit or world save, the the data is saved into the appropriate files.

Now, in the appropriate directory, simply rename the old **LocalPlayer.arkprofile** (or **steamid.arkprofile**) to something like **LocalPlayer.old.arkprofile**. You can rename it whatever you like; I like using **.old** and even **.old-MO-DD-YY-TIME** to differentiate between them. Once the old .arkprofile file is renamed, add in the generated file to this directory and rename it to **LocalPlayer.arkprofile** (or **steamid.arkprofile** if on a server). Boot up the game.

!!! Important
    **You won't see any changes you made (except for a few like character name) to a profile reflected on the character, until the character is respawned.**

    This is because there are two locations relevant to player character data. The first is from the **.arkprofile** file, and the second is in the world save file (**.ark**) where an instance of the player character is. Respawning creates a new instance of the character based on the data that was inside the **.arkprofile** file.

- - -

## More

If you'd like to see more, you've got two options. You can read the [API Documentation](arkmodule.md) to learn what methods and properties are available to you. Or, you can head on over to the [Tutorials](tutorials.md) to see much longer and complete examples using Arkpy.

If there's anything that is confusing and you think could be explained better, please leave an issue on Github labeled **docs**.