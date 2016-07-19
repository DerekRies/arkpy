File Format Specifications
===

This section will attempt to explain the binary file formats for the `.arkprofile`, `.arktribe`, and `.arkcharactersetting` file extensions. As well as the structure of the primitive data-types used in the files.

- - -

## Directory Structure

Soon

- - -

## Primitive Data Types

### Property

|     Field     |      Type      |
|---------------|----------------|
| Name          | Null Terminated String |
| Property Type | Null Terminated String |
| Size of Value | Int32                  |
| Index         | Int32                  |
| Value         | Specified Type         |

### ArrayProperty

|     Field     |      Type      |
|---------------|----------------|
| Name          | Null Terminated String |
| 'ArrayProperty' | Null Terminated String |
| Child Property Type | Null Terminated String |
| Size of Value | Int32                  |
| Index         | Int32                  |
| Values         | Specified Type (In Array Form)        |

### Struct

|     Field     |      Type      |
|---------------|----------------|
| Name          | Null Terminated String |
| Property Type | Null Terminated String |
| Size of Value | Int32                  |
| Index         | Int32                  |
| Struct Subclass | Null Terminated String |
| Values         | N <Property\>         |
