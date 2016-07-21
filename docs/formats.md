File Format Specifications
===

This section will attempt to explain the binary file formats for the `.arkprofile`, `.arktribe`, and `.arkcharactersetting` file extensions. As well as the structure of the primitive data-types used in the files.

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

- - -

## Primitive Data Types

For most of the file types the data is structued using the following primitives. Each one of these has the first two fields in common, Name and Property Type. So, we can read two length-prefixed null-terminated strings, with the first being the variable name and the second being the property type. Now that we know the property type to use we can read in the rest of the data following the structures below.

The 'Included in Array' column refers to which values are present when this property type is inside of an ArrayProperty.

### Property
(Int16Property, IntProperty, Int64Property, UInt16Property, UInt32Property, UInt64Property, FloatProperty, StrProperty, ByteProperty)

|     Field     |      Type      | Included in Array |
|---------------|----------------|-------------------|
| Name          | Length-Prefixed Null Terminated String | no |
| Property Type | Length-Prefixed Null Terminated String | no |
| Size of Value | Integer (32 Bits)                  | no |
| Index         | Integer (32 Bits)                  | no |
| Value         | Specified Type         | **yes** |

### ObjectProperty

|     Field     |      Type      | Included in Array |
|---------------|----------------|-------------------|
| Name          | Length-Prefixed Null Terminated String | no |
| Property Type | Length-Prefixed Null Terminated String | no |
| Size of Value | Integer (32 Bits)                  | no |
| Index         | Integer (32 Bits)                  | no |
| Quantity         | Integer (32 Bits)                  | **yes** |
| Value | Length-Prefixed Null Terminated String | **yes** |

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

### StructProperty

|     Field     |      Type      | Included in Array |
|---------------|----------------|-------------------|
| Name          | Length-Prefixed Null Terminated String | no |
| Property Type | Length-Prefixed Null Terminated String | no |
| Size of Value | Integer (32 Bits)                  | no |
| Index         | Integer (32 Bits)                  | no |
| Struct Subclass | Length-Prefixed Null Terminated String | no |
| Values         | N <Property\>         | **yes** |
| 'None' | Length-Prefixed Null Terminated String | **yes** |

Then there are some StructProperty subclasses that don't include the 'None' at the end or key,value property form, like the following:

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
