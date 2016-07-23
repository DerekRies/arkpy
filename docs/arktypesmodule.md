# `arkpy.arktypes` Module

The arktypes module contains all the data-type wrappers used by the ark file type readers and writers. Because all of them are wrappers around the python data-types, its important to use the .value property to read the data and the .set method to set the data on the Properties. Also, when applicable use the higher-level interfaces.

- - -


## `BaseProperty` Class
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

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `str`  | Initial value to set StrPropertys value to|
|**stream**| `BinaryStream` | (optional) A Binary stream that this StrProperty can build itself from |

  - **returns** a new `StrProperty`

**StrProperty.set**(value)

Casts value to a `str` if it isn't one already and sets StrProperty.value to this new string value.

| Parameter Name | Type | Description |
|------|------|-------------|
|**value** | `str`  | New value for StrProperty.value |

  - **returns** `None`

**StrProperty._calc_inner_size**()

Correctly calculates the size of this StrProperty's value. (Doesn't include the wrapped size)

 - **returns** `None`

**StrProperty._write_to_stream**(stream, array=False)

Writes this StrProperty to the BinaryStream that's been provided. If array is False then the entire contents of this property will be written (name, type, size, index, and value). If array is True however, then only the value will be written.

| Parameter Name | Type | Description |
|------|------|-------------|
|**stream** | `BinaryStream`  | A BinaryStream that this property can write its structure to |
|**array** | `bool`  | (optional) Flag specifying whether or not this property is being written inside of an Array. |


- - -
## `ArrayProperty` Class
### extends `BaseProperty`

Description

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the Array (in bytes), including the Int32 for length |
| **child_type**| `str` | The PropertyType of the items in the Array |
| **length**| `int` | The number of items in the array |
| **value**| `[]` | The python-list of all the actual values in the Array |

### **Methods**
- - -
## `ByteProperty` Class
### extends `BaseProperty`

Description

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | Size of the value, always 1 (Byte) |
| **value**| `char` | 8 bit integer or char with the actual value |

### **Methods**
- - -
## `ObjectProperty` Class
### extends `BaseProperty`

Description

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the Object (in bytes) including the Int32 for quantity and the value |
| **quantity**| `int` | Number of the object present |
| **value**| `str` | An entity-path string for the Object |

### **Methods**
- - -
## `FloatProperty` Class
### extends `BaseProperty`

A wrapper around the Float DataType.

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | Size of a Float, 4 Bytes |
| **value**| `float` | The actual Float value. Is a python float. |

### **Methods**
- - -
## `DoubleProperty` Class
### extends `BaseProperty`

Description

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | Size of a Double, 8 Bytes |
| **value**| `float` | The actual float value. Python floats are actually 64bit. |

### **Methods**
- - -
## `Int16Property` Class
### extends `BaseProperty`

Description

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the value, 2 Bytes |
| **value**| `int` | The actual value, which is a python integer, but is written and read as a 16 bit integer |

### **Methods**
- - -
## `UInt16Property` Class
### extends `BaseProperty`

Description

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the value, 2 Bytes |
| **value**| `int` | The actual value, which is a python integer, but is written and read as a 16 bit unsigned integer |

### **Methods**
- - -
## `IntProperty` Class
### extends `BaseProperty`

Description

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the value, 4 Bytes |
| **value**| `int` | The actual value, which is a python integer, but is written and read as a 32 bit integer |

### **Methods**
- - -
## `UInt32Property` Class
### extends `BaseProperty`

Description

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the value, 4 Bytes |
| **value**| `int` | The actual value, which is a python integer, but is written and read as a 32 bit unsigned integer |

### **Methods**
- - -
## `Int64Property` Class
### extends `BaseProperty`

Description

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the value, 8 Bytes |
| **value**| `int` | The actual value, which is a python integer, but is written and read as a 64 bit integer |

### **Methods**
- - -
## `UInt64Property` Class
### extends `BaseProperty`

Description

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the value, 8 Bytes |
| **value**| `int` | The actual value, which is a python integer, but is written and read as a 64 bit unsigned integer |

### **Methods**
- - -
## `BoolProperty` Class
### extends `BaseProperty`

Description

### **Properties**

| Name | Type | Description |
|------|------|-------------|
| **size** | `int` | The size of the value. **Heisenbug notice:** When written and read this value will be 0. But when structs with child BoolPropertys calculate their size, they need to assume the value size is 1, instead of 0. |
| **value**| `bool` | The actual Boolean value. |

### **Methods**
