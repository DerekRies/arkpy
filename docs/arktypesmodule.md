# `arkpy.arktypes` Module

The arktypes module contains all the data-type wrappers used by the ark file type readers and writers. Because all of them are wrappers around the python data-types, its important to use the .value property to read the data and the .set method to set the data on the Properties. Also, when applicable use the higher-level interfaces.

- - -
## `BaseProperty` Class

BaseProperty is an abstract class that is a low-level wrapper around python data-types and the data-types present in the Ark file formats. All other Property types derive from this Base Class.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **value**| `None` | Child Classes will define the type of this value |
| **size** | `int` | The size of the value in bytes |
| **index** | `int` | The index of this property, the default is 0, and only properties that are part of a `list` will increment this number. |
| **wrapped_size** | `int` | The total size of this property |
| **var_name** | `str` | The variable name for this property in whichever file it's being read from, or written to |
| **included** | `bool` | Flag specifying whether or not this property is included in size calculations and write operations |




- - -
## `BaseStruct` Class




- - -
## `StrProperty` Class
### extends `BaseProperty`

StrProperty is a low-level wrapper around the string data-type. Reads and writes a length-prefixed, null-terminated string. You probably won't need to instantiate new `StrProperty`s but they will be exposed by the FileType Wrappers like `ArkProfile`, and `ArkTribe`.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **value**| `str` | The actual string inside the StrProperty|
| **size** | `int` | The size of the string, including the length prefix and null byte|

### **Methods**

**StrProperty**(value='', stream=None)

Constructor method for creating StrPropertys. Can be instantiated with a value, or read from a `BinaryStream`.

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `str`  | Initial value to set StrPropertys value to|
|**stream**| `BinaryStream` | (optional) A Binary stream that this StrProperty can build itself from |

  - **returns** a new `StrProperty`

**set**(value)

Casts value to a `str` if it isn't one already and sets StrProperty.value to this new string value.

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `str`  | New value for StrProperty.value |

  - **returns** `None`

**_calc_inner_size**()

**(Internal Method)** Correctly calculates the size of this StrProperty's value. (Doesn't include the wrapped size)

 - **returns** `None`

**_write_to_stream**(stream, array=False)

**(Internal Method)** Writes this StrProperty to the BinaryStream that's been provided. If array is False then the entire contents of this property will be written (name, type, size, index, and value). If array is True however, then only the value will be written.

| Parameter Name | Type | Description |
|------|------|-------------|
|**stream** | `BinaryStream`  | A BinaryStream that this property can write its structure to |
|**array** | `bool`  | (optional) Flag specifying whether or not this property is being written inside of an Array. |




- - -
## `ArrayProperty` Class
### extends `BaseProperty`

ArrayProperty is a low-level wrapper around the python `list` datatype. Reads and writes a length prefixed array of properties. You probably won't need to instantiate new `ArrayProperty`s but they will be exposed by the FileType Wrappers like `ArkProfile`, and `ArkTribe`.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the Array (in bytes), including the Int32 for length |
| **child_type**| `str` | The PropertyType of the items in the Array |
| **length**| `int` | The number of items in the array |
| **value**| `list` | The python-list of all the actual values in the Array |

### **Methods**

**ArrayProperty**(child_type='IntProperty', stream=None)

Constructor method for creating ArrayProperty. Can be instantiated as empty, or read from a `BinaryStream`.

| Parameter Name | Type | Description |
|------|------|-------------|
|**child_type** | `str`  | (optional) Property type for the array members |
|**stream**| `BinaryStream` | (optional) A Binary stream that this StrProperty can build itself from |

  - **returns** a new `ArrayProperty`

**_calc_inner_size**()

**(Internal Method)** Correctly calculates the size of this ArrayProperty's value. Does so by including the inner-size of all the members of the array, and adding in the 4 Bytes for the length integer. (Doesn't include the wrapped size)

 - **returns** `int` - The number of bytes for the inner size

**_calc_wrapper_size**()

**(Internal Method)** Correctly calculates the size of this ArrayProperty's wrapper. The wrapper includes the Variable Name, Child Type string, ArrayProperty string, size integer, and index integer. (Doesn't include the inner size)

 - **returns** `int` - The number of bytes for the wrapper size

**_calc_size**()

**(Internal Method)** Correctly calculates the total size of this ArrayProperty. Includes the wrapper size and the inner size.

 - **returns** `int` - The number of bytes for the entire ArrayPropertys wrapped size

**_write_to_stream**(stream)

**(Internal Method)** Writes this ArrayProperty to the BinaryStream that's been provided.

| Parameter Name | Type | Description |
|------|------|-------------|
|**stream** | `BinaryStream`  | A BinaryStream that this property can write its structure to |




- - -
## `ByteProperty` Class
### extends `BaseProperty`

ByteProperty is a low-level wrapper around the python `int` data-type. Reads and writes an 8 bit integer, or char. You probably won't need to instantiate new `ByteProperty`s but they will be exposed by the FileType Wrappers like `ArkProfile`, and `ArkTribe`.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | Size of the value, always 1 (Byte) |
| **value**| `int` | 8 bit integer or char with the actual value |

### **Methods**

**ByteProperty**(value=0, stream=None, index=0)

Constructor method for creating a `ByteProperty`. Can be instantiated with a value, or read from a `BinaryStream`

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `int`  | (optional) An integer (keep it within 8 bits) that this ByteProperty's value will be set to |
|**index** | `int`  | (optional) Sets this ByteProperty's index to this |
|**stream** | `BinaryStream`  | (optional) A Binary stream that this ByteProperty can build itself from |

  - **returns** a new `ByteProperty`

**set**(value)

Casts value to an `int` if it isn't one already and sets ByteProperty.value to this new value.

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `int`  | New value for ByteProperty.value |

  - **returns** `None`

**_calc_size**()

**(Internal Method)** Correctly calculates the total size of this ByteProperty. Includes the wrapper size, inner size, and the junk NTString 'None' that is inserted into BytePropertys.

 - **returns** `int` - The number of bytes for the entire ByteProperty wrapped size

**_write_to_stream**(stream, array=False)

**(Internal Method)** Writes this ByteProperty to the BinaryStream that's been provided. If array is False then the entire contents of this property will be written (name, type, size, index, and value). If array is True however, then only the value will be written.

| Parameter Name | Type | Description |
|------|------|-------------|
|**stream** | `BinaryStream`  | A BinaryStream that this property can write its structure to |
|**array** | `bool`  | (optional) Flag specifying whether or not this property is being written inside of an Array. |





- - -
## `ObjectProperty` Class
### extends `BaseProperty`

ObjectProperty is a low-level wrapper around Arks object convention, which is a string for the value and an int describing quantity. You probably won't need to instantiate new `ObjectProperty`s unless you are adding to an ArrayProperty[ObjectProperty] like Engrams, or to a list of ObjectProperties like DefaultSlots. But, they will be exposed by the FileType Wrappers like `ArkProfile`, and `ArkTribe`.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the Object (in bytes) including the Int32 for quantity and the value |
| **quantity**| `int` | Number of the object present |
| **value**| `str` | An entity-path string for the Object |

### **Methods**

**ObjectProperty**(value='', stream=None, index=0)

Constructor method for creating a `ObjectProperty`. Can be instantiated with a value, or read from a `BinaryStream`

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `str`  | (optional) A string that this ObjectProperty's value will be set to. ObjectProperty values are almost always an Entity Path. |
|**index** | `int`  | (optional) Sets this ObjectProperty's index to this |
|**stream** | `BinaryStream`  | (optional) A Binary stream that this ObjectProperty can build itself from |

  - **returns** a new `ObjectProperty`

**set**(value)

Casts value to a `str` if it isn't one already and sets ObjectProperty.value to this new string value.

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `str`  | New value for ObjectProperty.value |

  - **returns** `None`

**_calc_inner_size**()

**(Internal Method)** Correctly calculates the size of this ObjectProperty's value + the quantity int. (Doesn't include the wrapped size)

 - **returns** `None`

**_write_to_stream**(stream, array=False)

**(Internal Method)** Writes this ObjectProperty to the BinaryStream that's been provided. If array is False then the entire contents of this property will be written (name, type, size, index, and value). If array is True however, then only the value will be written.

| Parameter Name | Type | Description |
|------|------|-------------|
|**stream** | `BinaryStream`  | A BinaryStream that this property can write its structure to |
|**array** | `bool`  | (optional) Flag specifying whether or not this property is being written inside of an Array. |




- - -
## `FloatProperty` Class
### extends `BaseProperty`

FloatProperty is a low-level wrapper around the python `float` data-type. Reads and writes an 32 bit float. You probably won't need to instantiate new `FloatProperty`s but they will be exposed by the FileType Wrappers like `ArkProfile`, and `ArkTribe`.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | Size of a Float, 4 Bytes |
| **value**| `float` | The actual Float value. Is a python float. |

### **Methods**

**FloatProperty**(value=0.0, stream=None, index=0)

Constructor method for creating a `FloatProperty`. Can be instantiated with a value, or read from a `BinaryStream`

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `float`  | (optional) A float that this FloatProperty's value will be set to. |
|**index** | `int`  | (optional) Sets this FloatProperty's index to this |
|**stream** | `BinaryStream`  | (optional) A Binary stream that this FloatProperty can build itself from |

  - **returns** a new `FloatProperty`

**set**(value)

Casts value to a `float` if it isn't one already and sets FloatProperty.value to this new string value.

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `float`  | New value for FloatProperty.value |

  - **returns** `None`

**_write_to_stream**(stream, array=False)

**(Internal Method)** Writes this FloatProperty to the BinaryStream that's been provided. If array is False then the entire contents of this property will be written (name, type, size, index, and value). If array is True however, then only the value will be written.

| Parameter Name | Type | Description |
|------|------|-------------|
|**stream** | `BinaryStream`  | A BinaryStream that this property can write its structure to |
|**array** | `bool`  | (optional) Flag specifying whether or not this property is being written inside of an Array. |

  - **returns** `None`




- - -
## `DoubleProperty` Class
### extends `BaseProperty`

DoubleProperty is a low-level wrapper around the python `float` data-type. Reads and writes an 64 bit float (double). You probably won't need to instantiate new `DoubleProperty`s but they will be exposed by the FileType Wrappers like `ArkProfile`, and `ArkTribe`.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | Size of a Double, 8 Bytes |
| **value**| `float` | The actual float value. Python floats are actually 64bit. |

### **Methods**

**DoubleProperty**(value=0.0, stream=None)

Constructor method for creating a `DoubleProperty`. Can be instantiated with a value, or read from a `BinaryStream`

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `float`  | (optional) A float that this DoubleProperty's value will be set to. |
|**stream** | `BinaryStream`  | (optional) A Binary stream that this DoubleProperty can build itself from |

  - **returns** a new `DoubleProperty`

**set**(value)

Casts value to a `float` if it isn't one already and sets DoubleProperty.value to this new string value.

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `float`  | New value for DoubleProperty.value |

  - **returns** `None`

**_write_to_stream**(stream, array=False)

**(Internal Method)** Writes this DoubleProperty to the BinaryStream that's been provided. If array is False then the entire contents of this property will be written (name, type, size, index, and value). If array is True however, then only the value will be written.

| Parameter Name | Type | Description |
|------|------|-------------|
|**stream** | `BinaryStream`  | A BinaryStream that this property can write its structure to |
|**array** | `bool`  | (optional) Flag specifying whether or not this property is being written inside of an Array. |

  - **returns** `None`




- - -
## `Int16Property` Class
### extends `BaseProperty`

Int16Property is a low-level wrapper around the python `int` data-type. Reads and writes a 16 bit integer. You probably won't need to instantiate new `Int16Property`s but they will be exposed by the FileType Wrappers like `ArkProfile`, and `ArkTribe`.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the value, 2 Bytes |
| **value**| `int` | The actual value, which is a python integer, but is written and read as a 16 bit integer |

### **Methods**

**Int16Property**(value=0, stream=None)

Constructor method for creating a `Int16Property`. Can be instantiated with a value, or read from a `BinaryStream`

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `int`  | (optional) A int that this Int16Property's value will be set to. |
|**stream** | `BinaryStream`  | (optional) A Binary stream that this Int16Property can build itself from |

  - **returns** a new `Int16Property`

**set**(value)

Casts value to a `int` if it isn't one already and sets Int16Property.value to this new string value.

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `int`  | New value for Int16Property.value |

  - **returns** `None`

**_write_to_stream**(stream, array=False)

**(Internal Method)** Writes this Int16Property to the BinaryStream that's been provided. If array is False then the entire contents of this property will be written (name, type, size, index, and value). If array is True however, then only the value will be written.

| Parameter Name | Type | Description |
|------|------|-------------|
|**stream** | `BinaryStream`  | A BinaryStream that this property can write its structure to |
|**array** | `bool`  | (optional) Flag specifying whether or not this property is being written inside of an Array. |

  - **returns** `None`




- - -
## `UInt16Property` Class
### extends `BaseProperty`

UInt16Property is a low-level wrapper around the python `int` data-type. Reads and writes a 16 bit unsigned integer. You probably won't need to instantiate new `UInt16Property`s but they will be exposed by the FileType Wrappers like `ArkProfile`, and `ArkTribe`.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the value, 2 Bytes |
| **value**| `int` | The actual value, which is a python integer, but is written and read as a 16 bit unsigned integer |

### **Methods**

**UInt16Property**(value=0, stream=None)

Constructor method for creating a `UInt16Property`. Can be instantiated with a value, or read from a `BinaryStream`

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `int`  | (optional) A int that this UInt16Property's value will be set to. |
|**stream** | `BinaryStream`  | (optional) A Binary stream that this UInt16Property can build itself from |

  - **returns** a new `UInt16Property`

**set**(value)

Casts value to a `int` if it isn't one already and sets UInt16Property.value to this new string value.

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `int`  | New value for UInt16Property.value |

  - **returns** `None`

**_write_to_stream**(stream, array=False)

**(Internal Method)** Writes this UInt16Property to the BinaryStream that's been provided. If array is False then the entire contents of this property will be written (name, type, size, index, and value). If array is True however, then only the value will be written.

| Parameter Name | Type | Description |
|------|------|-------------|
|**stream** | `BinaryStream`  | A BinaryStream that this property can write its structure to |
|**array** | `bool`  | (optional) Flag specifying whether or not this property is being written inside of an Array. |

  - **returns** `None`




- - -
## `IntProperty` Class
### extends `BaseProperty`

IntProperty is a low-level wrapper around the python `int` data-type. Reads and writes a 32 bit integer. You probably won't need to instantiate new `IntProperty`s but they will be exposed by the FileType Wrappers like `ArkProfile`, and `ArkTribe`.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the value, 4 Bytes |
| **value**| `int` | The actual value, which is a python integer, but is written and read as a 32 bit integer |

### **Methods**

**IntProperty**(value=0, stream=None)

Constructor method for creating a `IntProperty`. Can be instantiated with a value, or read from a `BinaryStream`

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `int`  | (optional) A int that this IntProperty's value will be set to. |
|**stream** | `BinaryStream`  | (optional) A Binary stream that this IntProperty can build itself from |

  - **returns** a new `IntProperty`

**set**(value)

Casts value to a `int` if it isn't one already and sets IntProperty.value to this new string value.

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `int`  | New value for IntProperty.value |

  - **returns** `None`

**_write_to_stream**(stream, array=False)

**(Internal Method)** Writes this IntProperty to the BinaryStream that's been provided. If array is False then the entire contents of this property will be written (name, type, size, index, and value). If array is True however, then only the value will be written.

| Parameter Name | Type | Description |
|------|------|-------------|
|**stream** | `BinaryStream`  | A BinaryStream that this property can write its structure to |
|**array** | `bool`  | (optional) Flag specifying whether or not this property is being written inside of an Array. |

  - **returns** `None`




- - -
## `UInt32Property` Class
### extends `BaseProperty`

UInt32Property is a low-level wrapper around the python `int` data-type. Reads and writes a 32 bit unsigned integer. You probably won't need to instantiate new `UInt32Property`s but they will be exposed by the FileType Wrappers like `ArkProfile`, and `ArkTribe`.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the value, 4 Bytes |
| **value**| `int` | The actual value, which is a python integer, but is written and read as a 32 bit unsigned integer |

### **Methods**

**UInt32Property**(value=0, stream=None)

Constructor method for creating a `UInt32Property`. Can be instantiated with a value, or read from a `BinaryStream`

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `int`  | (optional) A int that this UInt32Property's value will be set to. |
|**stream** | `BinaryStream`  | (optional) A Binary stream that this UInt32Property can build itself from |

  - **returns** a new `UInt32Property`

**set**(value)

Casts value to a `int` if it isn't one already and sets UInt32Property.value to this new string value.

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `int`  | New value for UInt32Property.value |

  - **returns** `None`

**_write_to_stream**(stream, array=False)

**(Internal Method)** Writes this UInt32Property to the BinaryStream that's been provided. If array is False then the entire contents of this property will be written (name, type, size, index, and value). If array is True however, then only the value will be written.

| Parameter Name | Type | Description |
|------|------|-------------|
|**stream** | `BinaryStream`  | A BinaryStream that this property can write its structure to |
|**array** | `bool`  | (optional) Flag specifying whether or not this property is being written inside of an Array. |

  - **returns** `None`




- - -
## `Int64Property` Class
### extends `BaseProperty`

Int64Property is a low-level wrapper around the python `int` data-type. Reads and writes a 64 bit integer. You probably won't need to instantiate new `Int64Property`s but they will be exposed by the FileType Wrappers like `ArkProfile`, and `ArkTribe`.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the value, 8 Bytes |
| **value**| `int` | The actual value, which is a python integer, but is written and read as a 64 bit integer |

### **Methods**

**Int64Property**(value=0, stream=None)

Constructor method for creating a `Int64Property`. Can be instantiated with a value, or read from a `BinaryStream`

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `int`  | (optional) A int that this Int64Property's value will be set to. |
|**stream** | `BinaryStream`  | (optional) A Binary stream that this Int64Property can build itself from |

  - **returns** a new `Int64Property`

**set**(value)

Casts value to a `int` if it isn't one already and sets Int64Property.value to this new string value.

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `int`  | New value for Int64Property.value |

  - **returns** `None`

**_write_to_stream**(stream, array=False)

**(Internal Method)** Writes this Int64Property to the BinaryStream that's been provided. If array is False then the entire contents of this property will be written (name, type, size, index, and value). If array is True however, then only the value will be written.

| Parameter Name | Type | Description |
|------|------|-------------|
|**stream** | `BinaryStream`  | A BinaryStream that this property can write its structure to |
|**array** | `bool`  | (optional) Flag specifying whether or not this property is being written inside of an Array. |

  - **returns** `None`




- - -
## `UInt64Property` Class
### extends `BaseProperty`

UInt64Property is a low-level wrapper around the python `int` data-type. Reads and writes a 64 bit unsigned integer. You probably won't need to instantiate new `UInt64Property`s but they will be exposed by the FileType Wrappers like `ArkProfile`, and `ArkTribe`.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the value, 8 Bytes |
| **value**| `int` | The actual value, which is a python integer, but is written and read as a 64 bit unsigned integer |

### **Methods**

**UInt64Property**(value=0, stream=None)

Constructor method for creating a `UInt64Property`. Can be instantiated with a value, or read from a `BinaryStream`

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `int`  | (optional) A int that this UInt64Property's value will be set to. |
|**stream** | `BinaryStream`  | (optional) A Binary stream that this UInt64Property can build itself from |

  - **returns** a new `UInt64Property`

**set**(value)

Casts value to a `int` if it isn't one already and sets UInt64Property.value to this new string value.

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `int`  | New value for UInt64Property.value |

  - **returns** `None`

**_write_to_stream**(stream, array=False)

**(Internal Method)** Writes this UInt64Property to the BinaryStream that's been provided. If array is False then the entire contents of this property will be written (name, type, size, index, and value). If array is True however, then only the value will be written.

| Parameter Name | Type | Description |
|------|------|-------------|
|**stream** | `BinaryStream`  | A BinaryStream that this property can write its structure to |
|**array** | `bool`  | (optional) Flag specifying whether or not this property is being written inside of an Array. |

  - **returns** `None`




- - -
## `BoolProperty` Class
### extends `BaseProperty`

BoolProperty is a low-level wrapper around the python `int` data-type. Reads and writes a Boolean value. You probably won't need to instantiate new `BoolProperty`s but they will be exposed by the FileType Wrappers like `ArkProfile`, and `ArkTribe`.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the value. **Heisenbug notice:** When written and read this value will be 0. But when structs with child BoolPropertys calculate their size, they need to assume the value size is 1, instead of 0. |
| **value**| `bool` | The actual Boolean value. |

### **Methods**

**BoolProperty**(value=True, stream=None)

Constructor method for creating a `BoolProperty`. Can be instantiated with a value, or read from a `BinaryStream`

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `bool`  | (optional) A bool that this BoolProperty's value will be set to. |
|**stream** | `BinaryStream`  | (optional) A Binary stream that this BoolProperty can build itself from |

  - **returns** a new `BoolProperty`

**set**(value)

Casts value to a `bool` if it isn't one already and sets BoolProperty.value to this new boolean value.

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `bool`  | New value for BoolProperty.value |

  - **returns** `None`

**_calc_size**()

**(Internal Method)** Calculates the total size of this BoolProperty, the wrapped size and the inner size. Although when files are written and read the inner size is 0; When parent containers like ArrayProperty or StructProperty calculate their size with a child BoolProperty the innersize needs to be 1 rather than 0.

  - **returns** `int` Total size in bytes for this BoolProperty

**_write_to_stream**(stream, array=False)

**(Internal Method)** Writes this BoolProperty to the BinaryStream that's been provided. If array is False then the entire contents of this property will be written (name, type, size, index, and value). If array is True however, then only the value will be written.

| Parameter Name | Type | Description |
|------|------|-------------|
|**stream** | `BinaryStream`  | A BinaryStream that this property can write its structure to |
|**array** | `bool`  | (optional) Flag specifying whether or not this property is being written inside of an Array. |

  - **returns** `None`

- - -
# Structs

- - -
## `PrimalPlayerDataStruct` Class
### extends `BaseStruct`
- - -
## `UniqueNetIDRepl` Class
### extends `BaseStruct`
- - -
## `PrimalPlayerCharacterConfigStruct` Class
### extends `BaseStruct`
- - -
## `PrimalPersistentCharacterStatsStruct` Class
### extends `BaseStruct`
- - -
## `TribeData` Class
### extends `BaseStruct`
- - -
## `TribeGovernment` Class
### extends `BaseStruct`
- - -
## `TribeAlliance` Class
### extends `BaseStruct`
- - -
## `LinearColor` Class
### extends `BaseStruct`