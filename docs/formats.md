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

**Note: Ark files are in Little-Endian**
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