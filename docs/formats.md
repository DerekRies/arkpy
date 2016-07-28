File Format Specifications
===

This section will attempt to explain the binary file formats for the `.arkprofile`, `.arktribe`, and `.arkcharactersetting` file extensions. As well as the structure of the primitive data-types used in the files. Some familiarity with basic Data Types and Hex Editors is assumed.

If you open any of the aforementioned file types in a Hex Editor, like 010 Editor or HxD, you'll see a bunch of strings (if it's set to display text) in the right hand side (like below).


```python
00C0h: 00 54 72 69 62 65 44 61 74 61 00 0F 00 00 00 53  .TribeData.....S
00D0h: 74 72 75 63 74 50 72 6F 70 65 72 74 79 00 4E 2A  tructProperty.N*
00E0h: 00 00 00 00 00 00 0A 00 00 00 54 72 69 62 65 44  ..........TribeD
00F0h: 61 74 61 00 0A 00 00 00 54 72 69 62 65 4E 61 6D  ata.....TribeNam
0100h: 65 00 0C 00 00 00 53 74 72 50 72 6F 70 65 72 74  e.....StrPropert
0110h: 79 00 0D 00 00 00 00 00 00 00 09 00 00 00 52 65  y.............Re
0120h: 66 75 67 65 65 73 00                             fugees.
```

The data is already fairly easy to understand, as there are many strings with the word 'Property' at the end of them. These identifiers let us know how to read in the proper data types. All these primitive data types will first be explained before going on to the individual file types.

!!! Note
    Ark files are in Little-Endian
- - -

## Primitive Data Types

For most of the file types the data is structued using the following primitives. Each one of these has the first two fields in common, Name and Property Type. So, we can read two length-prefixed null-terminated strings, with the first being the variable name and the second being the property type. Now that we know the property type to use we can read in the rest of the data following the structures below.

The 'Included in Array' column refers to which values are present when this property type is inside of an ArrayProperty.

### Property
(Int16Property, IntProperty, Int64Property, UInt16Property, UInt32Property, UInt64Property, FloatProperty, StrProperty, ByteProperty, BoolProperty)

|     Field     |      Type      | Included in Array |
|---------------|----------------|-------------------|
| Name          | Length-Prefixed Null Terminated String | no |
| Property Type | Length-Prefixed Null Terminated String | no |
| Size of Value | Integer (32 Bits)                  | no |
| Index         | Integer (32 Bits)                  | no |
| Value         | Specified Type         | **yes** |

**Example**:
```python
0324h: 14 00 00 00 50 6C 61 79 65 72 43 68 61 72 61 63  ....PlayerCharac
0334h: 74 65 72 4E 61 6D 65 00 0C 00 00 00 53 74 72 50  terName.....StrP
0344h: 72 6F 70 65 72 74 79 00 0C 00 00 00 00 00 00 00  roperty.........
0354h: 08 00 00 00 57 6F 6F 62 6C 65 73 00              ....Woobles.
```

1. In the example above we can see the variable name, **PlayerCharacterName** which is a length-prefixed (first byte represents the length of the string), null-terminated (ends with a null **0x00** byte) string.
1. Immediately following is another length-prefixed null-terminated string (here on out referred to as NTString) containing the property type, in this case **StrProperty**.
1. After the property type is the size of the value, **0x0C**, which in the case of strings is the number of bytes for the whole NTString (including the 32Bit Integer with the length of the string).
1. Then we have the Index, which is the distinguishing value between properties with the same variable name. In this case the Index value is 0. The next example, under ObjectProperty will show the Index in action.
1. After, the index is the actual value of the property, and in the case of a StrProperty that value is a NTString.

- - -


### ObjectProperty

|     Field     |      Type      | Included in Array |
|---------------|----------------|-------------------|
| Name          | Length-Prefixed Null Terminated String | no |
| Property Type | Length-Prefixed Null Terminated String | no |
| Size of Value | Integer (32 Bits)                  | no |
| Index         | Integer (32 Bits)                  | no |
| Quantity         | Integer (32 Bits)                  | **yes** |
| Value | Length-Prefixed Null Terminated String | **yes** |

**Example:**
```python
3BF7h: 23 00 00 00 50 6C 61 79 65 72 53 74 61 74 65 5F  #...PlayerState_
3C07h: 44 65 66 61 75 6C 74 49 74 65 6D 53 6C 6F 74 43  DefaultItemSlotC
3C17h: 6C 61 73 73 65 73 00 0F 00 00 00 4F 62 6A 65 63  lasses.....Objec
3C27h: 74 50 72 6F 70 65 72 74 79 00 81 00 00 00 00 00  tProperty.......
3C37h: 00 00 01 00 00 00 79 00 00 00 42 6C 75 65 70 72  ......y...Bluepr
3C47h: 69 6E 74 47 65 6E 65 72 61 74 65 64 43 6C 61 73  intGeneratedClas
3C57h: 73 20 2F 47 61 6D 65 2F 50 72 69 6D 61 6C 45 61  s /Game/PrimalEa
3C67h: 72 74 68 2F 43 6F 72 65 42 6C 75 65 70 72 69 6E  rth/CoreBlueprin
3C77h: 74 73 2F 57 65 61 70 6F 6E 73 2F 50 72 69 6D 61  ts/Weapons/Prima
3C87h: 6C 49 74 65 6D 5F 57 65 61 70 6F 6E 4D 65 74 61  lItem_WeaponMeta
3C97h: 6C 50 69 63 6B 2E 50 72 69 6D 61 6C 49 74 65 6D  lPick.PrimalItem
3CA7h: 5F 57 65 61 70 6F 6E 4D 65 74 61 6C 50 69 63 6B  _WeaponMetalPick
3CB7h: 5F 43 00 23 00 00 00 50 6C 61 79 65 72 53 74 61  _C.#...PlayerSta
3CC7h: 74 65 5F 44 65 66 61 75 6C 74 49 74 65 6D 53 6C  te_DefaultItemSl
3CD7h: 6F 74 43 6C 61 73 73 65 73 00 0F 00 00 00 4F 62  otClasses.....Ob
3CE7h: 6A 65 63 74 50 72 6F 70 65 72 74 79 00 87 00 00  jectProperty.‡..
3CF7h: 00 01 00 00 00 01 00 00 00 7F 00 00 00 42 6C 75  ............Blu
3D07h: 65 70 72 69 6E 74 47 65 6E 65 72 61 74 65 64 43  eprintGeneratedC
3D17h: 6C 61 73 73 20 2F 47 61 6D 65 2F 50 72 69 6D 61  lass /Game/Prima
3D27h: 6C 45 61 72 74 68 2F 43 6F 72 65 42 6C 75 65 70  lEarth/CoreBluep
3D37h: 72 69 6E 74 73 2F 57 65 61 70 6F 6E 73 2F 50 72  rints/Weapons/Pr
3D47h: 69 6D 61 6C 49 74 65 6D 5F 57 65 61 70 6F 6E 4D  imalItem_WeaponM
3D57h: 65 74 61 6C 48 61 74 63 68 65 74 2E 50 72 69 6D  etalHatchet.Prim
3D67h: 61 6C 49 74 65 6D 5F 57 65 61 70 6F 6E 4D 65 74  alItem_WeaponMet
3D77h: 61 6C 48 61 74 63 68 65 74 5F 43 00              alHatchet_C.
```
So at first glance there's a bit to unpack here, so let's go through step by step.

1. Starts with the variable name as an NTString, **PlayerState_DefaultItemSlotClasses**.
1. Then the property type as an NTString, **ObjectProperty**
1. The size of the Object, **0x81**
1. The index of the Object, **0x00**
1. The quantity of the Object, **0x01**
1. Finally we have the value as an NTString, **BlueprintGeneratedClass /Game/PrimalEarth/CoreBlueprints/Weapons/PrimalItem_WeaponMetalPick.PrimalItem_WeaponMetalPick_C**
1. Next it looks like we have another Object Property so we can repeat steps 1-6 again.

Both of the ObjectProperties have the same name, **PlayerState_DefaultItemSlotClasses**. However they are differentiated by their Index values. The first ObjectProperty has an index value of 0, while the second has an index value of 1. In this particular example, these Indices are referring to the slot that the particular item belongs to. A Metal Pick in the first slot, and a Metal Hatchet in the second. Refer to the fields possible index values in the File Specifications later to see what the Index refers to in that case.
- - -

### ArrayProperty

|     Field     |      Type      | Included in Array |
|---------------|----------------|-------------------|
| Name          | Length-Prefixed Null Terminated String | n/a |
| 'ArrayProperty' | Length-Prefixed Null Terminated String | n/a |
| Size of Value | Integer (32 Bits)                  | n/a |
| Index         | Integer (32 Bits)                  | n/a |
| Child Property Type | Length-Prefixed Null Terminated String | n/a |
| Length (Number of Values) | Integer (32 Bits)                  | n/a |
| Values         | Specified Type (In Array Form)        | n/a |

**Example**:
```python
018Eh: 19 00 00 00 42 6F 6E 65 4D 6F 64 69 66 69 65 72  ....BoneModifier
019Eh: 53 6C 69 64 65 72 56 61 6C 75 65 73 00 0E 00 00  SliderValues....
01AEh: 00 41 72 72 61 79 50 72 6F 70 65 72 74 79 00 5C  .ArrayProperty.\
01BEh: 00 00 00 00 00 00 00 0E 00 00 00 46 6C 6F 61 74  ...........Float
01CEh: 50 72 6F 70 65 72 74 79 00 16 00 00 00 00 00 00  Property........
01DEh: 3F 00 00 00 3F 00 00 00 3F 00 00 00 3F 5F 0B A4  ?...?...?...?_.¤
01EEh: 3D 00 00 00 3F 00 00 00 3F 00 00 00 3F 00 00 00  =...?...?...?...
01FEh: 3F 00 00 00 3F 00 00 00 3F 00 00 00 3F 00 00 00  ?...?...?...?...
020Eh: 3F 00 00 00 3F 00 00 00 3F 00 00 00 3F 00 00 00  ?...?...?...?...
021Eh: 3F 00 00 00 3F 00 00 00 3F 00 00 00 3F 00 00 00  ?...?...?...?...
022Eh: 3F 00 00 00 3F                                   ?...?
```

Like all other properties, the first four fields are the Name, PropertyType, Size, and Index. **However** it's important to remember that the size field in the ArrayProperty is not the number of items in the array, but the number of bytes that all the items take up. The Child Property type immediately following the index value, in this example **FloatProperty**, and the length of the array, `0x16000000` or 22 in Decimal, should inform you of how to read in the following values. Inside the array, the only things present will be the value and perhaps another field (refer to the Included in Array column in the tables).

So, in this example we have 22 Floats, of which 21 of them are `0x0000003F` or 0.5 as a Float. And the size of the array is `0x5C` (92 in Decimal), which can be calculated by multiplying the size of the child type, c, with the number of items, n, and adding 4 (the Int32 representing the length of the array).

```
Size = c*n + 4
     = 4*22 + 4
     = 92
```
- - -

### StructProperty

|     Field     |      Type      | Included in Array |
|---------------|----------------|-------------------|
| Name          | Length-Prefixed Null Terminated String | no |
| Property Type | Length-Prefixed Null Terminated String | no |
| Size of Value | Integer (32 Bits)                  | no |
| Index         | Integer (32 Bits)                  | no |
| Struct Type | Length-Prefixed Null Terminated String | no |
| Values         | N <Property\>         | **yes** |
| 'None' | Length-Prefixed Null Terminated String | **yes** |


**Example:**
```python
025Dh: 10 00 00 00 54 72 69 62 65 47 6F 76 65 72 6E 6D  ....TribeGovernm
026Dh: 65 6E 74 00 0F 00 00 00 53 74 72 75 63 74 50 72  ent.....StructPr
027Dh: 6F 70 65 72 74 79 00 4A 00 00 00 00 00 00 00 10  operty.J........
028Dh: 00 00 00 54 72 69 62 65 47 6F 76 65 72 6E 6D 65  ...TribeGovernme
029Dh: 6E 74 00 21 00 00 00 54 72 69 62 65 47 6F 76 65  nt.!...TribeGove
02ADh: 72 6E 5F 44 69 6E 6F 55 6E 63 6C 61 69 6D 41 64  rn_DinoUnclaimAd
02BDh: 6D 69 6E 4F 6E 6C 79 00 0C 00 00 00 49 6E 74 50  minOnly.....IntP
02CDh: 72 6F 70 65 72 74 79 00 04 00 00 00 00 00 00 00  roperty.........
02DDh: 01 00 00 00 05 00 00 00 4E 6F 6E 65 00           ........None.
```

1. Name as NTString, **TribeGovernment**
2. Type as NTString, **StructProperty**
3. Size of struct values, **0x4A**
4. Index, **0x00**
5. Struct Type as NTString, **TribeGovernment**
6. Values (Follow the same procedure as any other property)
    1. Name as NTString, **TribeGovern_DinoUnclaimAdminOnly**
    2. Property as NTString, **IntProperty**
    3. Value as Int32, **0x04**
7. Termined with **'None'** as NTString

Structs will exclude data from values if that value is a default value. In the previous example you can see there is only one property 'TribeGovern_DinoUnclaimAdminOnly', there should be 4 others on this particular struct. They are excluded because they are the default value.


Then there are some StructProperty SubTypes. that don't include the 'None' at the end or key,value property form, like the following:


### LinearColor

|     Field     |      Type      | Included in Array |
|---------------|----------------|-------------------|
| Name          | Length-Prefixed Null Terminated String | no |
| Property Type | Length-Prefixed Null Terminated String | no |
| Size of Value | Integer (32 Bits)                  | no |
| Index         | Integer (32 Bits)                  | no |
| 'LinearColor' | Length-Prefixed Null Terminated String | no |
| Red         | Float         | **yes** |
| Green         | Float         | **yes** |
| Blue         | Float         | **yes** |
| Alpha         | Float         | **yes** |

**Example:**

```python
02D4h: 0B 00 00 00 42 6F 64 79 43 6F 6C 6F 72 73 00 0F  ....BodyColors..
02E4h: 00 00 00 53 74 72 75 63 74 50 72 6F 70 65 72 74  ...StructPropert
02F4h: 79 00 10 00 00 00 01 00 00 00 0C 00 00 00 4C 69  y.............Li
0304h: 6E 65 61 72 43 6F 6C 6F 72 00 CD CC CC 3D CD CC  nearColor.ÍÌÌ=ÍÌ
0314h: CC 3D CD CC CC 3D 00 00 80 3F                    Ì=ÍÌÌ=..€?
```

In this example, following the NTString **LinearColor** (the struct type), there are four float values packed into the 16 Bytes that make up the size of the Struct.

All the Struct Types specific to File Types will be displayed in the appropriate section for that File Type.
- - -

## File Types

The structure of the .arkcharactersetting, .arkprofile, and .arktribe files are all pretty close in structure. They start with a similar header, and then are followed by a single container Struct, that represents all the data in the file.

For each file type I'll start off with the Header, show a simple example of what it would look like in a Hex Editor, and then describe it's contents. Then, I will show an example of the hex contents inside the body and list the structs that can be found in the file type, starting with the parent container struct.

These files often exclude chunks of data that are default, so in many cases there will be data missing in these files. In the Struct descriptions I will include all of their child properties and their default values if applicable. Also I will not be describing the structs Byte by Byte, but rather Property by Property. So if you are not familiar yet with the Property structure Ark uses refer back to the previous section.

!!! Note
    All Files are Terminated with a NTString 'None' and 4 NULL Bytes
- - -

## .arkcharactersetting

These files describe the templates, or saved presets, that you can choose to quickly create a character off of on the character creation screen. They are relatively simple and contain no compressed data.

**Header**

```python
0000h: 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
0010h: 00 00 00 00 17 00 00 00 50 72 69 6D 61 6C 43 68  ........PrimalCh
0020h: 61 72 61 63 74 65 72 53 65 74 74 69 6E 67 00 01  aracterSetting..
0030h: 00 00 00 04 00 00 00 19 00 00 00 50 72 69 6D 61  ...........Prima
0040h: 6C 43 68 61 72 61 63 74 65 72 53 65 74 74 69 6E  lCharacterSettin
0050h: 67 5F 30 00 0C 00 00 00 53 70 61 77 6E 55 49 5F  g_0.....SpawnUI_
0060h: 43 5F 31 00 16 00 00 00 53 68 6F 6F 74 65 72 47  C_1.....ShooterG
0070h: 61 6D 65 49 6E 73 74 61 6E 63 65 5F 30 00 10 00  ameInstance_0...
0080h: 00 00 53 68 6F 6F 74 65 72 45 6E 67 69 6E 65 5F  ..ShooterEngine_
0090h: 30 00 00 00 00 00 00 00 00 00 00 00 00 00 A6 00  0.............¦.
00A0h: 00 00 00 00 00 00                                ......
```

| Field | Type | Size (Bytes) | Description |
|--------|-------|----------------|-------|
| **Unknown** | Int32 | 4 | this is probably a either a Start Flag or a versioning Integer for the file. |
| PADDING | NULL | 16 | 16 NULL Bytes for padding |
| **File Type** | NTString | 20 | For this file it is always **PrimalCharacterSetting**|
| **Unknown** | Int32 | 4 | value is always 1|
| **Unknown** | Int32 | 4 | Strong suspicion that this number refers to the number of NTStrings that will follow |
| **File Number** | NTString | 5+n | this value is always equal to **PrimalCharacterSetting_X**, where **X** is the number of the file. **(n)** in the Size Column refers to the number of characters in the string. |
| **Unknown** | NTString | 5+n | **SpawnUI_C_1** is the only value I've observed. It's possible this value varies in SOTF or other conversions |
| **Unknown** | NTString | 5+n | **ShooterGameInstance_0** is the only value I've observed. It's possible this value varies in SOTF or other conversions |
| **Unknown** | NTString | 5+n | **ShooterEngine_0** is the only value I've observed. It's possible this value varies in SOTF or other conversions |
| PADDING | NULL | 12 | 12 NULL Bytes for padding |
| **Header Size** | Int32 | 4 | The size of the header in bytes. Also the start position of the container struct |
| PADDING | NULL | 4 | 4 Null Bytes for padding |

**Structs**

```python
00A6h: 11 00 00 00 43 68 61 72 61 63 74 65 72 53 65 74  ....CharacterSet
00B6h: 74 69 6E 67 00 0F 00 00 00 53 74 72 75 63 74 50  ting.....StructP
00C6h: 72 6F 70 65 72 74 79 00 52 01 00 00 00 00 00 00  roperty.R.......
00D6h: 10 00 00 00 43 68 61 72 61 63 74 65 72 50 72 65  ....CharacterPre
00E6h: 73 65 74 00 15 00 00 00 42 6F 64 79 43 6F 6C 6F  set.....BodyColo
00F6h: 72 53 6C 69 64 65 72 56 61 6C 75 65 00 0E 00 00  rSliderValue....
0106h: 00 46 6C 6F 61 74 50 72 6F 70 65 72 74 79 00 04  .FloatProperty..
0116h: 00 00 00 00 00 00 00 00 00 00 3F 15 00 00 00 48  ..........?....H
0126h: 61 69 72 43 6F 6C 6F 72 53 6C 69 64 65 72 56 61  airColorSliderVa
0136h: 6C 75 65 00 0E 00 00 00 46 6C 6F 61 74 50 72 6F  lue.....FloatPro
0146h: 70 65 72 74 79 00 04 00 00 00 00 00 00 00 00 00  perty...........
0156h: 00 3F 14 00 00 00 45 79 65 43 6F 6C 6F 72 53 6C  .?....EyeColorSl
0166h: 69 64 65 72 56 61 6C 75 65 00 0E 00 00 00 46 6C  iderValue.....Fl
0176h: 6F 61 74 50 72 6F 70 65 72 74 79 00 04 00 00 00  oatProperty.....
0186h: 00 00 00 00 00 00 00 3F 19 00 00 00 42 6F 6E 65  .......?....Bone
0196h: 4D 6F 64 69 66 69 65 72 53 6C 69 64 65 72 56 61  ModifierSliderVa
01A6h: 6C 75 65 73 00 0E 00 00 00 41 72 72 61 79 50 72  lues.....ArrayPr
01B6h: 6F 70 65 72 74 79 00 5C 00 00 00 00 00 00 00 0E  operty.\........
01C6h: 00 00 00 46 6C 6F 61 74 50 72 6F 70 65 72 74 79  ...FloatProperty
01D6h: 00 16 00 00 00 00 00 00 3F 00 00 00 3F 00 00 00  ........?...?...
01E6h: 3F 00 00 00 3F 5F 0B A4 3D 00 00 00 3F 00 00 00  ?...?_.¤=...?...
01F6h: 3F 00 00 00 3F 00 00 00 3F 00 00 00 3F 00 00 00  ?...?...?...?...
0206h: 3F 00 00 00 3F 00 00 00 3F 00 00 00 3F 00 00 00  ?...?...?...?...
0216h: 3F 00 00 00 3F 00 00 00 3F 00 00 00 3F 00 00 00  ?...?...?...?...
0226h: 3F 00 00 00 3F 00 00 00 3F 00 00 00 3F 05 00 00  ?...?...?...?...
0236h: 00 4E 6F 6E 65 00 05 00 00 00 4E 6F 6E 65 00 00  .None.....None..
0246h: 00 00 00                                         ...
```

CharacterPreset<Struct\> **CharacterSetting** (Container Struct)

| Name | Property Type | Default Value |
|------|---------------|-------------|
| **BodyColorSliderValue** | FloatProperty (0.0-1.0) | 0.5 |
| **HairColorSliderValue** | FloatProperty (0.0-1.0) | 0.5 |
| **EyeColorSliderValue** | FloatProperty (0.0-1.0) | 0.5 |
| **BoneModifierSliderValue** | ArrayProperty [FloatProperty] (0.0-1.0) | 0.5 |


- - -

## .arkprofile

!!! Important
    This section refers to any **LocalPlayer.arkprofile**, or **SteamID.arkprofile** but not the **PlayerLocalData.arkprofile** file as that follows a different structure

.arkprofile files contain all the data relevant to the player character, apart from things handled at the world level like Inventory and Position.

**Header**

```python
0000h: 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00  ................
0010h: 00 00 00 00 00 00 00 00 11 00 00 00 50 72 69 6D  ............Prim
0020h: 61 6C 50 6C 61 79 65 72 44 61 74 61 00 00 00 00  alPlayerData....
0030h: 00 05 00 00 00 14 00 00 00 50 72 69 6D 61 6C 50  .........PrimalP
0040h: 6C 61 79 65 72 44 61 74 61 5F 32 31 00 0C 00 00  layerData_21....
0050h: 00 41 72 6B 47 61 6D 65 4D 6F 64 65 00 10 00 00  .ArkGameMode....
0060h: 00 50 65 72 73 69 73 74 65 6E 74 4C 65 76 65 6C  .PersistentLevel
0070h: 00 0A 00 00 00 54 68 65 49 73 6C 61 6E 64 00 26  .....TheIsland.&
0080h: 00 00 00 2F 47 61 6D 65 2F 4D 61 70 73 2F 54 68  .../Game/Maps/Th
0090h: 65 49 73 6C 61 6E 64 53 75 62 4D 61 70 73 2F 54  eIslandSubMaps/T
00A0h: 68 65 49 73 6C 61 6E 64 00 00 00 00 00 00 00 00  heIsland........
00B0h: 00 00 00 00 00 BD 00 00 00 00 00 00 00           .....½.......
```

| Field | Type | Size (Bytes) | Description |
|--------|-------|----------------|-------|
| **Unknown** | Int32 | 4 | this is probably a either a Start Flag |
| **Unknown** | Int32 | 4 | this is probably a versioning Integer for the file. All .arkprofile files with the exception of PlayerLocalData.arkprofile have a value of 1 |
| PADDING | NULL | 16 | 16 NULL Bytes for padding |
| **File Type** | NTString | 21 | For this file it is always **PrimalPlayerData**|
| **Unknown** | Int32 | 4 | value is always 0|
| **Unknown** | Int32 | 4 | Strong suspicion that this number refers to the number of NTStrings that will follow |
| **File Number** | NTString | 5+n | this value is always equal to **PrimalPlayerData_X**, where **X** is the number of the file. **(n)** in the Size Column refers to the number of characters in the string. |
| **Unknown** | NTString | 5+n | **ArkGameMode** is the only value I've observed. |
| **Game Mode** | NTString | 5+n | **PersistentLevel** is the only value I've observed. It's possible this value varies in SOTF or other conversions |
| **Map Name** | NTString | 5+n | **TheIsland** or **TheCenter**. Not sure what the value is on Unofficial modded maps, but it is probably whatever name was specified by the mod.|
| **Map Path** | NTString | 5+n | The asset path for the map this character is on. **/Game/Maps/TheIslandSubMaps/TheIsland** |
| PADDING | NULL | 12 | 12 NULL Bytes for padding |
| **Header Size** | Int32 | 4 | The size of the header in bytes. Also the start position of the container struct |
| PADDING | NULL | 4 | 4 Null Bytes for padding |


**Structs**

```
00BFh: 07 00 00 00 4D 79 44 61 74 61 00 0F 00 00 00 53  ....MyData.....S
00CFh: 74 72 75 63 74 50 72 6F 70 65 72 74 79 00 C1 02  tructProperty.Á.
00DFh: 00 00 00 00 00 00 17 00 00 00 50 72 69 6D 61 6C  ..........Primal
00EFh: 50 6C 61 79 65 72 44 61 74 61 53 74 72 75 63 74  PlayerDataStruct
00FFh: 00 0D 00 00 00 50 6C 61 79 65 72 44 61 74 61 49  .....PlayerDataI
010Fh: 44 00 0F 00 00 00 55 49 6E 74 36 34 50 72 6F 70  D.....UInt64Prop
011Fh: 65 72 74 79 00 08 00 00 00 00 00 00 00 45 5C 56  erty.........E\V
012Fh: 00 00 00 00 00 09 00 00 00 55 6E 69 71 75 65 49  .........UniqueI
013Fh: 44 00 0F 00 00 00 53 74 72 75 63 74 50 72 6F 70  D.....StructProp
014Fh: 65 72 74 79 00 1A 00 00 00 00 00 00 00 10 00 00  erty............
015Fh: 00 55 6E 69 71 75 65 4E 65 74 49 64 52 65 70 6C  .UniqueNetIdRepl
016Fh: 00 08 00 00 00 12 00 00 00 31 31 31 31 31 31 31  .........1111111
017Fh: 31 31 31 31 31 31 31 31 31 31 00 14 00 00 00 53  1111111111.....S
018Fh: 61 76 65 64 4E 65 74 77 6F 72 6B 41 64 64 72 65  avedNetworkAddre
019Fh: 73 73 00 0C 00 00 00 53 74 72 50 72 6F 70 65 72  ss.....StrProper
01AFh: 74 79 00 16 00 00 00 00 00 00 00 12 00 00 00 31  ty.............1
01BFh: 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31 31  1111111111111111
01CFh: 00 0B 00 00 00 50 6C 61 79 65 72 4E 61 6D 65 00  .....PlayerName.
01DFh: 0C 00 00 00 53 74 72 50 72 6F 70 65 72 74 79 00  ....StrProperty.
01EFh: 0C 00 00 00 00 00 00 00 08 00 00 00 43 61 73 73  ............Cass
01FFh: 69 75 73 00 18 00 00 00 4D 79 50 6C 61 79 65 72  ius.....MyPlayer
020Fh: 43 68 61 72 61 63 74 65 72 43 6F 6E 66 69 67 00  CharacterConfig.
021Fh: 0F 00 00 00 53 74 72 75 63 74 50 72 6F 70 65 72  ....StructProper
022Fh: 74 79 00 E7 00 00 00 00 00 00 00 22 00 00 00 50  ty.ç......."...P
023Fh: 72 69 6D 61 6C 50 6C 61 79 65 72 43 68 61 72 61  rimalPlayerChara
024Fh: 63 74 65 72 43 6F 6E 66 69 67 53 74 72 75 63 74  cterConfigStruct
025Fh: 00 0B 00 00 00 42 6F 64 79 43 6F 6C 6F 72 73 00  .....BodyColors.
026Fh: 0F 00 00 00 53 74 72 75 63 74 50 72 6F 70 65 72  ....StructProper
027Fh: 74 79 00 10 00 00 00 00 00 00 00 0C 00 00 00 4C  ty.............L
028Fh: 69 6E 65 61 72 43 6F 6C 6F 72 00 66 66 86 3F 66  inearColor.ff†?f
029Fh: 66 66 3F 29 5C 4F 3F 00 00 80 3F 0B 00 00 00 42  ff?)\O?..€?....B
02AFh: 6F 64 79 43 6F 6C 6F 72 73 00 0F 00 00 00 53 74  odyColors.....St
02BFh: 72 75 63 74 50 72 6F 70 65 72 74 79 00 10 00 00  ructProperty....
02CFh: 00 01 00 00 00 0C 00 00 00 4C 69 6E 65 61 72 43  .........LinearC
02DFh: 6F 6C 6F 72 00 66 66 86 3F 66 66 66 3F 29 5C 4F  olor.ff†?fff?)\O
02EFh: 3F 00 00 80 3F 0B 00 00 00 42 6F 64 79 43 6F 6C  ?..€?....BodyCol
02FFh: 6F 72 73 00 0F 00 00 00 53 74 72 75 63 74 50 72  ors.....StructPr
030Fh: 6F 70 65 72 74 79 00 10 00 00 00 02 00 00 00 0C  operty..........
031Fh: 00 00 00 4C 69 6E 65 61 72 43 6F 6C 6F 72 00 0A  ...LinearColor..
032Fh: D7 A3 3D F5 F3 A6 3D 27 83 63 3D 00 00 80 3F 05  ×£=õó¦='ƒc=..€?.
033Fh: 00 00 00 4E 6F 6E 65 00 09 00 00 00 41 70 70 49  ...None.....AppI
034Fh: 44 53 65 74 00 0E 00 00 00 41 72 72 61 79 50 72  DSet.....ArrayPr
035Fh: 6F 70 65 72 74 79 00 08 00 00 00 00 00 00 00 0C  operty..........
036Fh: 00 00 00 49 6E 74 50 72 6F 70 65 72 74 79 00 01  ...IntProperty..
037Fh: 00 00 00 36 BA 05 00 12 00 00 00 50 6C 61 79 65  ...6º......Playe
038Fh: 72 44 61 74 61 56 65 72 73 69 6F 6E 00 0C 00 00  rDataVersion....
039Fh: 00 49 6E 74 50 72 6F 70 65 72 74 79 00 04 00 00  .IntProperty....
03AFh: 00 00 00 00 00 01 00 00 00 05 00 00 00 4E 6F 6E  .............Non
03BFh: 65 00 05 00 00 00 4E 6F 6E 65 00 00 00 00 00     e.....None.....
```

SteamID and IP Address replaced with 1s.

PrimalPlayerDataStruct<StructProperty\> **MyData** (Container Struct)

| Name | Property Type | Default Value |
|------|---------------|-------------|
| **PlayerDataID** | UInt64Property | n/a |
| **UniqueID** | UniqueNetIdRepl<StructProperty> | n/a |
| **SavedNetworkAddress** | StrProperty | None |
| **PlayerName** | StrProperty | None |
| **bFirstSpawned** | BoolProperty | False |
| **MyPlayerCharacterConfig** | PrimalPlayerCharacterConfigStruct<StructProperty> | n/a |
| **MyPersistentCharacterStats** | PrimalPersistentCharacterStatsStruct<StructProperty> | n/a |
| **TribeID** | IntProperty | None |
| **PlayerDataVersion** | IntProperty | 1 (But this value isn't excluded) |
| **AppIDSet** | ArrayProperty[IntProperty] | [375350] (But this value isn't ex cluded) |



UniqueNetIDRepl<StructProperty\> **UniqueID**

Is a smaller struct like LinearColor<StructProperty> in that it doesnt have a series of named properties and is instead represented byte by byte in the following way:

|     Field     |      Type      | Included in Array |
|---------------|----------------|-------------------|
| Name          | NTString | no |
| Property Type | NTString | no |
| Size of Value | Integer (32 Bits)                  | no |
| Index         | Integer (32 Bits)                  | no |
| 'UniqueNetIDRepl' | NTString | no |
| Unknown         | Integer (32 Bits)         | no |
| Value         | NTString (steam id) | no |




PrimalPlayerCharacterConfigStruct<StructProperty\> **MyPlayerCharacterConfig**

| Name | Property Type | Default Value |
|------|---------------|-------------|
| **BodyColors** | List of LinearColor<StructProperty\>. Not ArrayProperty, just index-differentiated | n/a |
| **RawBoneModifiers** | List of FloatPropertys (0.0-1.0). Not ArrayProperty, just index-differentiated | 0.5 |
| **bIsFemale** | BoolProperty | False |
| **PlayerCharacterName** | StrProperty | None |
| **PlayerSpawnRegionIndex** | IntProperty | 1 (But this value isn't excluded) |


PrimalPersistentCharacterStatsStruct<StructProperty\> **MyPersistentCharacterStats**

| Name | Property Type | Default Value |
|------|---------------|-------------|
| **CharacterStatusComponent_ExtraCharacterLevel** | UInt16Property | 0 |
| **CharacterStatusComponent_ExperiencePoints** | FloatProperty | 0.0 |
| **PlayerState_TotalEngramPoints** | IntProperty | 0 |
| **PlayerState_EngramBlueprints** | ArrayProperty [ObjectProperty] | [None] |
| **CharacterStatusComponent_NumberOfLevelUpPointsApplied** | List of BytePropertys. Not ArrayProperty, just index-differentiated | 0 |
| **PlayerState_DefaultItemSlotClasses** | List of ObjectPropertys. Not ArrayProperty, just index-differentiated | [None] |


- - -

## .arktribe

**Header**

```python
0000h: 01 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00  ................
0010h: 00 00 00 00 00 00 00 00 10 00 00 00 50 72 69 6D  ............Prim
0020h: 61 6C 54 72 69 62 65 44 61 74 61 00 00 00 00 00  alTribeData.....
0030h: 05 00 00 00 14 00 00 00 50 72 69 6D 61 6C 54 72  ........PrimalTr
0040h: 69 62 65 44 61 74 61 5F 33 33 33 00 0C 00 00 00  ibeData_333.....
0050h: 41 72 6B 47 61 6D 65 4D 6F 64 65 00 10 00 00 00  ArkGameMode.....
0060h: 50 65 72 73 69 73 74 65 6E 74 4C 65 76 65 6C 00  PersistentLevel.
0070h: 0A 00 00 00 54 68 65 49 73 6C 61 6E 64 00 26 00  ....TheIsland.&.
0080h: 00 00 2F 47 61 6D 65 2F 4D 61 70 73 2F 54 68 65  ../Game/Maps/The
0090h: 49 73 6C 61 6E 64 53 75 62 4D 61 70 73 2F 54 68  IslandSubMaps/Th
00A0h: 65 49 73 6C 61 6E 64 00 00 00 00 00 00 00 00 00  eIsland.........
00B0h: 00 00 00 00 BC 00 00 00 00 00 00 00              ....¼.......
```


| Field | Type | Size (Bytes) | Description |
|--------|-------|----------------|-------|
| **Unknown** | Int32 | 4 | this is probably a either a Start Flag |
| **Unknown** | Int32 | 4 | this is probably a versioning Integer for the file. Always a value of 1. |
| PADDING | NULL | 16 | 16 NULL Bytes for padding |
| **File Type** | NTString | 21 | For this file it is always **PrimalTribeData**|
| **Unknown** | Int32 | 4 | value is always 0|
| **Unknown** | Int32 | 4 | Strong suspicion that this number refers to the number of NTStrings that will follow |
| **File Number** | NTString | 5+n | this value is always equal to **PrimalTribeData_X**, where **X** is the number of the file. **(n)** in the Size Column refers to the number of characters in the string. |
| **Unknown** | NTString | 5+n | **ArkGameMode** is the only value I've observed. |
| **Game Mode** | NTString | 5+n | **PersistentLevel** is the only value I've observed. It's possible this value varies in SOTF or other conversions |
| **Map Name** | NTString | 5+n | **TheIsland** or **TheCenter**. Not sure what the value is on Unofficial modded maps, but it is probably whatever name was specified by the mod.|
| **Map Path** | NTString | 5+n | The asset path for the map this character is on. **/Game/Maps/TheIslandSubMaps/TheIsland** |
| PADDING | NULL | 12 | 12 NULL Bytes for padding |
| **Header Size** | Int32 | 4 | The size of the header in bytes. Also the start position of the container struct |
| PADDING | NULL | 4 | 4 Null Bytes for padding |

**Structs**

```
00BAh: 0A 00 00 00 54 72 69 62 65 44 61 74 61 00 0F 00  ....TribeData...
00CAh: 00 00 53 74 72 75 63 74 50 72 6F 70 65 72 74 79  ..StructProperty
00DAh: 00 AD 01 00 00 00 00 00 00 0A 00 00 00 54 72 69  .­...........Tri
00EAh: 62 65 44 61 74 61 00 0A 00 00 00 54 72 69 62 65  beData.....Tribe
00FAh: 4E 61 6D 65 00 0C 00 00 00 53 74 72 50 72 6F 70  Name.....StrProp
010Ah: 65 72 74 79 00 09 00 00 00 00 00 00 00 05 00 00  erty............
011Ah: 00 42 52 49 4F 00 12 00 00 00 4F 77 6E 65 72 50  .BRIO.....OwnerP
012Ah: 6C 61 79 65 72 44 61 74 61 49 44 00 0F 00 00 00  layerDataID.....
013Ah: 55 49 6E 74 33 32 50 72 6F 70 65 72 74 79 00 04  UInt32Property..
014Ah: 00 00 00 00 00 00 00 0C 61 48 00 08 00 00 00 54  ........aH.....T
015Ah: 72 69 62 65 49 44 00 0C 00 00 00 49 6E 74 50 72  ribeID.....IntPr
016Ah: 6F 70 65 72 74 79 00 04 00 00 00 00 00 00 00 12  operty..........
017Ah: 1B 80 54 12 00 00 00 4D 65 6D 62 65 72 73 50 6C  .€T....MembersPl
018Ah: 61 79 65 72 4E 61 6D 65 00 0E 00 00 00 41 72 72  ayerName.....Arr
019Ah: 61 79 50 72 6F 70 65 72 74 79 00 15 00 00 00 00  ayProperty......
01AAh: 00 00 00 0C 00 00 00 53 74 72 50 72 6F 70 65 72  .......StrProper
01BAh: 74 79 00 02 00 00 00 05 00 00 00 4B 4F 4E 59 00  ty.........KONY.
01CAh: 04 00 00 00 4D 61 78 00 14 00 00 00 4D 65 6D 62  ....Max.....Memb
01DAh: 65 72 73 50 6C 61 79 65 72 44 61 74 61 49 44 00  ersPlayerDataID.
01EAh: 0E 00 00 00 41 72 72 61 79 50 72 6F 70 65 72 74  ....ArrayPropert
01FAh: 79 00 0C 00 00 00 00 00 00 00 0F 00 00 00 55 49  y.............UI
020Ah: 6E 74 33 32 50 72 6F 70 65 72 74 79 00 02 00 00  nt32Property....
021Ah: 00 0C 61 48 00 F2 E2 B9 18 0C 00 00 00 54 72 69  ..aH.òâ¹.....Tri
022Ah: 62 65 41 64 6D 69 6E 73 00 0E 00 00 00 41 72 72  beAdmins.....Arr
023Ah: 61 79 50 72 6F 70 65 72 74 79 00 08 00 00 00 00  ayProperty......
024Ah: 00 00 00 0F 00 00 00 55 49 6E 74 33 32 50 72 6F  .......UInt32Pro
025Ah: 70 65 72 74 79 00 01 00 00 00 F2 E2 B9 18 0F 00  perty.....òâ¹...
026Ah: 00 00 62 53 65 74 47 6F 76 65 72 6E 6D 65 6E 74  ..bSetGovernment
027Ah: 00 0D 00 00 00 42 6F 6F 6C 50 72 6F 70 65 72 74  .....BoolPropert
028Ah: 79 00 00 00 00 00 00 00 00 00 01 05 00 00 00 4E  y..............N
029Ah: 6F 6E 65 00 05 00 00 00 4E 6F 6E 65 00 00 00 00  one.....None....
02AAh: 00                                               .
```


TribeData<StructProperty\> **TribeData** (Container Struct)

| Name | Property Type | Default Value |
|------|---------------|-------------|
| **TribeName** | StrProperty | None |
| **OwnerPlayerDataID** | UInt32Property | n/a |
| **TribeID** | IntProperty | n/a |
| **MembersPlayerName** | ArrayProperty [StrProperty] | [None] |
| **MembersPlayerDataID** | ArrayProperty [UInt32Property] | [None] |
| **bSetGovernment** | BoolProperty | False |
| **TribeAdmins** | ArrayProperty[UInt32Property] | [None] |
| **TribeAlliances** | ArrayProperty[AllianceStruct<StructProperty\>]| [None] |
| **TribeGovernment** | TribeGovernment<StructProperty\> | n/a |
| **MembersConfigs** | ArrayProperty[PrimalPlayerCharacterConfigStruct<StructProperty\>] | [None] |
| **TribeLog** | ArrayProperty [StrProperty] | [None] |
| **LogIndex** | IntProperty | 0 |


TribeAlliance<Struct\> [**TribeAlliance**]

| Name | Property Type | Default Value |
|------|---------------|-------------|
| **AllianceName** | StrProperty | n/a |
| **AllianceID** | UInt32Property | n/a |
| **MembersTribeName** | ArrayProperty[StrProperty] | n/a |
| **MembersTribeID** | ArrayProperty[UInt32Property] | n/a |
| **AdminsTribeID** | ArrayProperty[UInt32Property] | n/a |


TribeGovernment<Struct\> **TribeGovernment**

| Name | Property Type | Default Value |
|------|---------------|-------------|
| **TribeGovern_PINCode** | IntProperty | 0 |
| **TribeGovern_DinoOwnership** | IntProperty | 0 |
| **TribeGovern_StructureOwnership** | IntProperty | 0 |
| **TribeGovern_DinoUnclaimAdminOnly** | IntProperty | 0 |

