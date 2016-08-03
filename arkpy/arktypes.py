"""
arktypes is a collection of data structures used in the Ark: Survival
Evolved file formats. This includes subclasses of StructProperty as
well as the primitives used like FloatProperty or IntProperty because
in the file formats the usage of these primitives isn't the typical
bytesize of type + 1 Byte for identifier. Instead most of the primitives
are identified by string, and then have 8 bytes between the type string
and the value, which is usually the size of the structure (4 bytes),
the index (another 4 bytes).
"""

import random
import utils
import json
import itertools
import struct

from binary import BinaryStream

# debug = True
debug = False


def load_struct(stream):
    size = stream.readInt32()
    index = stream.readInt32()
    name = stream.readNullTerminatedString()
    struct = STRUCTS.get(name, BaseStruct)(stream=stream)
    # struct = STRUCTS[name](stream=stream)
    struct.size = size
    struct.index = index
    return struct


def load_property(stream):
    name, prop_type = stream.read_pair()
    # print (name, prop_type)
    if prop_type == 'StructProperty':
        return (name, prop_type, load_struct(stream))
    else:
        return (name, prop_type, PROPERTIES[prop_type](stream=stream))


class BaseProperty():

    def __init__(self, value=None):
        # print 'Base Property init'
        self.value = value
        self.index = 0
        self.size = 0
        self.wrapped_size = 0
        self.var_name = ''
        self.included = True
        self.changed = False

    def set(self, value):
        self.value = value

    def _write_shared_prop_info(self, stream):
        stream.writeNullTerminatedString(self.var_name)
        stream.writeNullTerminatedString(self.__class__.__name__)
        stream.writeInt32(self.size)
        stream.writeInt32(self.index)

    def _calc_inner_size(self):
        return self.size

    def _calc_wrapper_size(self):
        # 5 Bytes for each NTString
        ws = len(self.var_name) + len(self.__class__.__name__) + 10
        # 4 Bytes for two Int32s (innersize, index)
        ws = ws + 8
        return ws

    def _calc_size(self):
        if self.included:
            ws = self._calc_wrapper_size()
            self.wrapped_size = ws + self.size
            return self.wrapped_size
        else:
            return 0

    def __repr__(self):
        return '<%s> %s' % (self.__class__.__name__, self.value)


class BaseStruct:

    def __init__(self, stream=None):
        self.data = {}
        self.size = 0
        self.wrapped_size = 0
        self.index = 0
        self.var_name = ''
        self.included = True

        if stream is not None:
            while stream.peek(stream.readNullTerminatedString) != 'None':
                self.load_and_set_next_property(stream)
            stream.readNullTerminatedString()

    def get(self, key):
        return self.data[key]

    def set(self, key, value):
        if isinstance(value, list):
            for i in xrange(len(value)):
                value[i].var_name = key
        else:
            value.var_name = key
        self.data[key] = value

    def load_and_set_next_property(self, stream):
        """
        Reads and automatically sets the next property value to
        the appropriate field on the data dict of this struct. Since
        some fields in Ark File formats use the same name, but are not
        an array, their differentiator is a little Int32 index field.
        """
        name, prop_type, value = load_property(stream)
        value.var_name = name
        field = self.data.get(name, None)
        if field is None:
            self.data[name] = value
        else:
            if isinstance(field, list):
                utils.list_set(field, value.index, value)
            elif value.index > 0:
                prev_value = field
                self.data[name] = []
                utils.list_set(self.data[name], prev_value.index, prev_value)
                utils.list_set(self.data[name], value.index, value)
            else:
                if field.__class__.__name__ == 'ArrayProperty':
                    # TODO: Would like to merge arrays of structs with default
                    # values so that the proper structs will be used
                    pass
                self.data[name] = value
        if debug:
            print '----------------------------------------'
            print "Struct Type: %s" % self.__class__.__name__
            print self.data
            print '----------------------------------------'

    def _calc_inner_size(self):
        size = 0
        for key in self.data:
            if isinstance(self.data[key], list):
                for val in self.data[key]:
                    if val.included:
                        size = size + val._calc_size()
            else:
                if self.data[key].included:
                    # try:
                    size = size + self.data[key]._calc_size()
                    # except TypeError:
                    # print key
        # NTString 'None' Bytes included
        self.size = size + 9
        return self.size

    def _calc_wrapper_size(self):
        # 5 Bytes for each NTString
        ws = len(self.var_name) + len(self.__class__.__name__) + 10
        # 19 Bytes for StructProperty NTString
        ws = ws + 19
        # 4 Bytes for two Int32s (innersize, index)
        ws = ws + 8
        return ws

    def _calc_size(self):
        # A structs size is the sum of all its non-default children's
        # wrapped_sizes.
        # The wrapped size is the size of the value + the bytes for the
        # variable name, variable type, (and sub-type if struct+available)
        self._calc_inner_size()
        ws = self._calc_wrapper_size()
        self.wrapped_size = ws + self.size
        return self.wrapped_size

    def _write_shared_struct_info(self, stream):
        stream.writeNullTerminatedString(self.var_name)
        stream.writeNullTerminatedString('StructProperty')
        stream.writeInt32(self.size)
        stream.writeInt32(self.index)
        stream.writeNullTerminatedString(self.__class__.__name__)

    def _write_to_stream(self, stream, array=False):
        if self.included:
            self._calc_size()
            if array is False:
                self._write_shared_struct_info(stream)
            # for each field in the data dict, write it
            for key, value in self.data.iteritems():
                if isinstance(value, list):
                    for v in value:
                        if v is not None:
                            v._write_to_stream(stream)
                else:
                    value._write_to_stream(stream)
            stream.writeNullTerminatedString('None')

    def _exclude(self):
        pass


class StrProperty(BaseProperty):

    def __init__(self, value='', stream=None):
        BaseProperty.__init__(self)
        self.set(value=value)
        self.size = 5 + len(value)
        self._is_unicode = False
        if stream is not None:
            self.size = stream.readInt32()
            self.index = stream.readInt32()
            pos = stream.tell()
            try:
                self.value = stream.readNullTerminatedString()
            except struct.error:
                # TODO: Correctly parse Unicode string.
                self._is_unicode = True
                stream.base_stream.seek(pos, 0)
                unicode_str = stream.readBytes(self.size)
                self.value = unicode_str

    def set(self, value):
        self.value = str(value)
        self.size = 5 + len(self.value)

    def _calc_inner_size(self):
        self.size = 5 + len(self.value)
        return self.size

    def _write_to_stream(self, stream, array=False):
        if self.included:
            if array is False:
                self._write_shared_prop_info(stream)
            if self._is_unicode:
                stream.writeBytes(self.value)
            else:
                stream.writeNullTerminatedString(self.value)


class ArrayProperty(BaseProperty):

    def __init__(self, child_type='IntProperty', stream=None):
        BaseProperty.__init__(self)
        self.value = []
        # An ArrayProperty's size is not the length of items
        # It is the size of the array values in Bytes like every other
        # property/struct
        self.size = 4
        self.child_type = child_type
        self.length = 0
        if stream is not None:
            self._set_from_stream(stream)

    def _set_from_stream(self, stream):
        conversion_table = {
            'ByteProperty': stream.readChar,
            'IntProperty': stream.readInt32,
            'UIntProperty': stream.readUInt32,
            'UInt32Property': stream.readUInt32,
            'Int16Property': stream.readInt16,
            'UInt16Property': stream.readUInt16,
            'Int64Property': stream.readInt64,
            'UInt64Property': stream.readUInt64,
            'FloatProperty': stream.readFloat,
            'DoubleProperty': stream.readDouble,
            'StrProperty': stream.readNullTerminatedString,
            'ObjectProperty': stream.readNullTerminatedString,
        }
        self.size = stream.readInt32()
        self.index = stream.readInt32()
        self.child_type = stream.readNullTerminatedString()
        self.length = stream.readInt32()
        for i in xrange(self.length):
            if self.child_type == 'StructProperty':
                value = BaseStruct(stream)
                self.value.append(value)
            else:
                if self.child_type == 'ObjectProperty':
                    stream.readInt32()
                    value = stream.readNullTerminatedString()
                elif self.child_type == 'StrProperty':
                    # Special Case for StrProperty unicode string hack
                    # TODO: Refactor array child property reading to the
                    # property primitives, and refactor out property's reading
                    # from stream to its own method that can read from an array
                    # or not like the write methods do
                    pos = stream.tell()
                    try:
                        value = stream.readNullTerminatedString()
                    except struct.error:
                        print 'Exception in array string handling'
                        stream.base_stream.seek(pos, 0)
                        value = stream.readUnicodeString()
                else:
                    # value = conversion_table.get(self.child_type, BaseStruct)
                    value = conversion_table[self.child_type]()
                prop = PROPERTIES[self.child_type](value=value)
                self.value.append(prop)

    def __repr__(self):
        return "[]<%s>(%s)" % (self.child_type, self.length)

    def _calc_inner_size(self):
        print 'Calculating ArrayProperty Inner Size'
        size = 4
        for val in self.value:
            size = size + val._calc_inner_size()
        self.size = size
        return self.size

    def _calc_wrapper_size(self):
        # 5 Bytes for each NTString
        ws = len(self.var_name) + len(self.child_type) + 10
        # 18 Bytes for ArrayProperty NTString
        ws = ws + 18
        # 4 Bytes for two Int32s (innersize, index)
        ws = ws + 8
        return ws

    def _calc_size(self):
        if len(self.value) > 0:
            self._calc_inner_size()
            # Another 18 Bytes for ArrayProperty
            ws = self._calc_wrapper_size()
            self.wrapped_size = ws + self.size
            return self.wrapped_size
        else:
            return 0

    def _write_to_stream(self, stream):
        if len(self.value) > 0:
            stream.writeNullTerminatedString(self.var_name)
            stream.writeNullTerminatedString('ArrayProperty')
            stream.writeInt32(self.size)
            stream.writeInt32(self.index)
            stream.writeNullTerminatedString(self.child_type)
            stream.writeInt32(len(self.value))
            for val in self.value:
                val._write_to_stream(stream, array=True)


class ByteProperty(BaseProperty):

    def __init__(self, value=0, stream=None, index=0):
        BaseProperty.__init__(self)
        self.value = value
        self.index = index
        self.size = 1
        if stream is not None:
            self.size = stream.readInt32()
            self.index = stream.readInt32()
            # No idea why there's a junk "None" inserted here
            stream.readNullTerminatedString()
            self.value = stream.readChar()

    def set(self, value=0):
        self.value = int(value)

    def _calc_size(self):
        if self.included:
            ws = self._calc_wrapper_size()
            # NTString 'None' needs to be counted
            ws = ws + 9
            self.wrapped_size = ws + self.size
            return self.wrapped_size
        else:
            return 0

    def _write_to_stream(self, stream, array=False):
        if self.included:
            if array is False:
                self._write_shared_prop_info(stream)
                stream.writeNullTerminatedString('None')
            stream.writeChar(self.value)


class ObjectProperty(BaseProperty):

    def __init__(self, value='', stream=None, index=0):
        BaseProperty.__init__(self)
        self.index = index
        self.value = value
        self.quantity = 1
        if stream is not None:
            self.size = stream.readInt32()
            self.index = stream.readInt32()
            # No idea what this is, it's always 01 00 00 00 in the
            # ObjectProperties I've seen. Maybe it's an identifier
            # for the type of data to follow, like 1=String?
            self.quantity = stream.readInt32()
            self.value = stream.readNullTerminatedString()

    def set(self, value):
        self.value = value

    def _calc_inner_size(self):
        # 4 Bytes for Prefix (01 00 00 00)
        # 4 Bytes for string length
        # N Bytes for N length string
        # 1 NULL Byte to terminate string
        self.size = 9 + len(self.value)
        return self.size

    def _calc_size(self):
        if self.included:
            self._calc_inner_size()
            ws = self._calc_wrapper_size()
            self.wrapped_size = ws + self.size
            return self.wrapped_size
        else:
            return 0

    def _write_to_stream(self, stream, array=False):
        if self.included:
            if array is False:
                self._write_shared_prop_info(stream)
            stream.writeInt32(1)
            stream.writeNullTerminatedString(self.value)


class FloatProperty(BaseProperty):

    def __init__(self, value=0.0, stream=None, index=0):
        BaseProperty.__init__(self)
        self.set(value=value)
        self.size = 4
        self.index = index
        if stream is not None:
            self.size = stream.readInt32()
            self.index = stream.readInt32()
            self.value = stream.readFloat()

    def set(self, value=0.0):
        self.value = float(value)

    def _write_to_stream(self, stream, array=False):
        if self.included:
            if array is False:
                self._write_shared_prop_info(stream)
            stream.writeFloat(self.value)


class DoubleProperty(BaseProperty):

    def __init__(self, value=0.0, stream=None):
        BaseProperty.__init__(self)
        self.set(value=value)
        self.size = 8
        if stream is not None:
            self.size = stream.readInt32()
            self.index = stream.readInt32()
            self.value = stream.readDouble()

    def set(self, value=0.0):
        self.value = float(value)

    def _write_to_stream(self, stream, array=False):
        if self.included:
            if array is False:
                self._write_shared_prop_info(stream)
            stream.writeDouble(self.value)


class Int16Property(BaseProperty):

    def __init__(self, value=0, stream=None):
        BaseProperty.__init__(self)
        self.set(value=value)
        self.size = 2
        if stream is not None:
            self.size = stream.readInt32()
            self.index = stream.readInt32()
            self.value = stream.readInt16()

    def set(self, value=0):
        self.value = int(value)

    def _write_to_stream(self, stream, array=False):
        if self.included:
            if array is False:
                self._write_shared_prop_info(stream)
            stream.writeInt16(self.value)


class UInt16Property(BaseProperty):

    def __init__(self, value=0, stream=None):
        BaseProperty.__init__(self)
        self.set(value=value)
        self.size = 2
        if stream is not None:
            self.size = stream.readInt32()
            self.index = stream.readInt32()
            self.value = stream.readUInt16()

    def set(self, value=0):
        self.value = int(value)

    def _write_to_stream(self, stream, array=False):
        if self.included:
            if array is False:
                self._write_shared_prop_info(stream)
            stream.writeUInt16(self.value)


class IntProperty(BaseProperty):

    def __init__(self, value=0, stream=None):
        BaseProperty.__init__(self)
        self.set(value=value)
        self.size = 4
        if stream is not None:
            self.size = stream.readInt32()
            self.index = stream.readInt32()
            self.value = stream.readInt32()

    def set(self, value=0):
        self.value = int(value)

    def _write_to_stream(self, stream, array=False):
        if self.included:
            if array is False:
                self._write_shared_prop_info(stream)
            stream.writeInt32(self.value)


class UInt32Property(BaseProperty):

    def __init__(self, value=0, stream=None):
        BaseProperty.__init__(self)
        self.set(value=value)
        self.size = 4
        if stream is not None:
            self.size = stream.readInt32()
            self.index = stream.readInt32()
            self.value = stream.readUInt32()

    def set(self, value=0):
        self.value = int(value)

    def _write_to_stream(self, stream, array=False):
        if self.included:
            if array is False:
                self._write_shared_prop_info(stream)
            stream.writeUInt32(self.value)


class Int64Property(BaseProperty):

    def __init__(self, value=0, stream=None):
        BaseProperty.__init__(self)
        self.set(value=value)
        self.size = 8
        if stream is not None:
            self.size = stream.readInt32()
            self.index = stream.readInt32()
            self.value = stream.readInt64()

    def set(self, value=0):
        self.value = int(value)

    def _write_to_stream(self, stream, array=False):
        if self.included:
            if array is False:
                self._write_shared_prop_info(stream)
            stream.writeInt64(self.value)


class UInt64Property(BaseProperty):

    def __init__(self, value=0, stream=None):
        BaseProperty.__init__(self, value=value)
        self.set(value=value)
        self.size = 8
        if stream is not None:
            self.size = stream.readInt32()
            self.index = stream.readInt32()
            self.value = stream.readUInt64()

    def set(self, value=0):
        self.value = int(value)

    def _write_to_stream(self, stream, array=False):
        if self.included:
            if array is False:
                self._write_shared_prop_info(stream)
            stream.writeUInt64(self.value)


class BoolProperty(BaseProperty):

    def __init__(self, value=True, stream=None):
        BaseProperty.__init__(self)
        self.value = value
        self.size = 0
        if stream is not None:
            self.size = stream.readInt32()
            self.index = stream.readInt32()
            self.value = bool(stream.readChar())

    def set(self, value=True):
        self.value = bool(value)

    def _write_to_stream(self, stream, array=False):
        if self.value:
            if array is False:
                self._write_shared_prop_info(stream)
            stream.writeBool(self.value)

    def _calc_size(self):
        # BoolPropertys are a bit of a Heisenbug when it comes to
        # their size. When they are written their size value is always
        # 0, but their true size is of course 1 Byte. Because
        # when it comes time for structs and container properties like
        # ObjectProperty or ArrayProperty types to calculate their size
        # there will be 1 more Byte in the file than what the size says
        # it is, because the size and true size don't match.
        if self.value:
            ws = self._calc_wrapper_size()
            self.wrapped_size = ws + 1
            return self.wrapped_size
        else:
            return 0


# ArkProfile Structures ----------------------------------

class PrimalPlayerDataStruct(BaseStruct):

    def __init__(self, size=0, stream=None):
        BaseStruct.__init__(self)
        self.size = size
        self.var_name = 'MyData'

        # Default Values
        random_id = utils._gen_player_id()
        self.set('PlayerDataID', UInt64Property(value=random_id))
        self.set('UniqueID', UniqueNetIdRepl())
        self.set('SavedNetworkAddress', StrProperty())
        self.set('PlayerName', StrProperty())
        self.set('bFirstSpawned', BoolProperty())
        self.set('bIsSpectator', BoolProperty())
        cs = 'MyPlayerCharacterConfig'
        self.set(cs, PrimalPlayerCharacterConfigStruct())
        ss = 'MyPersistentCharacterStats'
        self.set(ss, PrimalPersistentCharacterStatsStruct())
        self.set('TribeID', IntProperty())
        self.set('PlayerDataVersion', IntProperty(value=1))
        self.set('AppIDSet', ArrayProperty(child_type='IntProperty'))
        self.data['AppIDSet'].value.append(IntProperty(value=375350))

        if stream is not None:
            while stream.peek(stream.readNullTerminatedString) != 'None':
                self.load_and_set_next_property(stream)
            stream.readNullTerminatedString()

    def _exclude(self):
        if self.data['SavedNetworkAddress'].value == '':
            self.data['SavedNetworkAddress'].included = False
        if self.data['TribeID'].value == 0:
            self.data['TribeID'].included = False
        self.data['MyPlayerCharacterConfig']._exclude()
        self.data['MyPersistentCharacterStats']._exclude()

    def _write_to_stream(self, stream):
        print 'calculating sizes'
        self._exclude()
        self._calc_size()
        print 'writing player data struct'
        self._write_shared_struct_info(stream)
        self.data['PlayerDataID']._write_to_stream(stream)
        self.data['UniqueID']._write_to_stream(stream)
        self.data['SavedNetworkAddress']._write_to_stream(stream)
        self.data['PlayerName']._write_to_stream(stream)
        self.data['bFirstSpawned']._write_to_stream(stream)
        self.data['bIsSpectator']._write_to_stream(stream)
        self.data['MyPlayerCharacterConfig']._write_to_stream(stream)
        self.data['MyPersistentCharacterStats']._write_to_stream(stream)
        self.data['TribeID']._write_to_stream(stream)
        self.data['AppIDSet']._write_to_stream(stream)
        self.data['PlayerDataVersion']._write_to_stream(stream)
        stream.writeNullTerminatedString('None')


class UniqueNetIdRepl(BaseStruct):

    def __init__(self, stream=None):
        BaseStruct.__init__(self)
        self.size = 26
        self.value = '00000000000000000'
        if stream is not None:
            stream.readInt32()
            self.value = stream.readNullTerminatedString()

    def set(self, value=''):
        self.value = str(value)

    def _write_to_stream(self, stream):
        self._write_shared_struct_info(stream)
        stream.writeInt32(8)
        stream.writeNullTerminatedString(self.value)

    def __repr__(self):
        return str(self.__class__.__name__) + ': ' + str(self.value)

    def _calc_size(self):
        self.size = len(self.value) + 9
        ws = self._calc_wrapper_size()
        self.wrapped_size = ws + self.size
        return self.wrapped_size


class PrimalPlayerCharacterConfigStruct(BaseStruct):

    def __init__(self, stream=None):
        BaseStruct.__init__(self)
        # Default Values
        # Setting the index values from the loop in the init
        # because EVERY other solution I tried, including closures
        # and seperate method calls resulted in the same scope
        # and assigning the same index value to every single list item
        colors = [LinearColor(index=i) for i in xrange(3)]
        self.set('BodyColors', colors)
        # self.set('BodyColors', [])
        self.set('PlayerCharacterName', StrProperty())
        bones = [FloatProperty(value=0.5, index=j) for j in xrange(22)]
        self.set('RawBoneModifiers', bones)
        # self.set('RawBoneModifiers', [])
        self.set('bIsFemale', BoolProperty(value=False))
        self.set('PlayerSpawnRegionIndex', IntProperty())

        if stream is not None:
            # Structs with multiple values end with None
            while stream.peek(stream.readNullTerminatedString) != 'None':
                self.load_and_set_next_property(stream)
            # Remember to read the None to advance position past it when done
            stream.readNullTerminatedString()

    def _exclude(self):
        # colors
        for bone in self.data['RawBoneModifiers']:
            if bone.value == 0.5 and not bone.changed:
                bone.included = False

    def _write_to_stream(self, stream):
        self._write_shared_struct_info(stream)
        for color in self.data['BodyColors']:
            color._write_to_stream(stream)
        self.data['PlayerCharacterName']._write_to_stream(stream)
        for bone in self.data['RawBoneModifiers']:
            bone._write_to_stream(stream)
        self.data['bIsFemale']._write_to_stream(stream)
        self.data['PlayerSpawnRegionIndex']._write_to_stream(stream)
        stream.writeNullTerminatedString('None')


class LinearColor(BaseStruct):

    def __init__(self, r=0.0, g=0.0, b=0.0, a=1.0, stream=None, index=0):
        BaseStruct.__init__(self)
        self.size = 16
        self.index = index
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        if stream is not None:
            self.r = stream.readFloat()
            self.g = stream.readFloat()
            self.b = stream.readFloat()
            self.a = stream.readFloat()

    def _calc_size(self):
        ws = self._calc_wrapper_size()
        self.wrapped_size = ws + self.size
        return self.wrapped_size

    def set(self, r=0.0, g=0.0, b=0.0, a=1.0):
        self.r = float(r)
        self.g = float(g)
        self.b = float(b)
        self.a = float(a)

    def __repr__(self):
        color_tuple = (self.r, self.g, self.b, self.a)
        return "(R: %s, G: %s, B: %s, A: %s)" % color_tuple

    def _write_to_stream(self, stream):
        if self.included:
            self._write_shared_struct_info(stream)
            stream.writeFloat(self.r)
            stream.writeFloat(self.g)
            stream.writeFloat(self.b)
            stream.writeFloat(self.a)


class PrimalPersistentCharacterStatsStruct(BaseStruct):

    def __init__(self, stream=None):
        BaseStruct.__init__(self)

        # Default Values
        csc_s = 'CharacterStatusComponent_'
        levels_string = csc_s + 'ExtraCharacterLevel'
        exp_string = csc_s + 'ExperiencePoints'
        level_up_string = csc_s + 'NumberOfLevelUpPointsApplied'

        self.set(levels_string, UInt16Property())
        self.set(exp_string, FloatProperty())
        self.set('PlayerState_TotalEngramPoints', IntProperty())
        learned_engrams = ArrayProperty(child_type='ObjectProperty')
        self.set('PlayerState_EngramBlueprints', learned_engrams)
        lvlups = [ByteProperty(index=i) for i in xrange(12)]
        self.set(level_up_string, lvlups)
        default_slots = [ObjectProperty(index=i) for i in xrange(10)]
        self.set('PlayerState_DefaultItemSlotClasses', default_slots)

        if stream is not None:
            while stream.peek(stream.readNullTerminatedString) != 'None':
                self.load_and_set_next_property(stream)
            stream.readNullTerminatedString()

    def _exclude(self):
        # Experience Points
        exp_string = 'CharacterStatusComponent_ExperiencePoints'
        if self.data[exp_string].value == 0.0:
            self.data[exp_string].included = False
        # Levels
        levels_string = 'CharacterStatusComponent_ExtraCharacterLevel'
        if self.data[levels_string].value == 0:
            self.data[levels_string].included = False
        # Engram Points
        if self.data['PlayerState_TotalEngramPoints'].value == 0:
            self.data['PlayerState_TotalEngramPoints'].included = False
        # Stat Points
        l = self.data['CharacterStatusComponent_NumberOfLevelUpPointsApplied']
        for lvlup in l:
            if lvlup.value == 0:
                lvlup.included = False
        # Default Slots
        for slot in self.data['PlayerState_DefaultItemSlotClasses']:
            if slot.value == '':
                slot.included = False

    def _write_to_stream(self, stream):
        self._write_shared_struct_info(stream)
        csc_s = 'CharacterStatusComponent_'
        levels_string = csc_s + 'ExtraCharacterLevel'
        exp_string = csc_s + 'ExperiencePoints'
        level_up_string = csc_s + 'NumberOfLevelUpPointsApplied'
        self.data[levels_string]._write_to_stream(stream)
        self.data[exp_string]._write_to_stream(stream)
        self.data['PlayerState_TotalEngramPoints']._write_to_stream(stream)
        self.data['PlayerState_EngramBlueprints']._write_to_stream(stream)
        for lvlup in self.data[level_up_string]:
            lvlup._write_to_stream(stream)
        for slot in self.data['PlayerState_DefaultItemSlotClasses']:
            slot._write_to_stream(stream)
        stream.writeNullTerminatedString('None')


# ArkTribe Structures

class TribeData(BaseStruct):

    def __init__(self, stream=None):
        BaseStruct.__init__(self)
        self.var_name = 'TribeData'

        random_id = utils._gen_tribe_id()
        self.set('TribeName', StrProperty())
        self.set('OwnerPlayerDataID', UInt32Property())
        self.set('TribeID', IntProperty(value=random_id))
        self.set('MembersPlayerName', ArrayProperty(child_type='StrProperty'))
        self.set('MembersPlayerDataID', ArrayProperty(
            child_type='UInt32Property'))
        self.set('MembersRankGroups', ArrayProperty(child_type='ByteProperty'))
        self.set('bSetGovernment', BoolProperty(value=False))
        self.set('TribeAdmins', ArrayProperty(child_type='UInt32Property'))
        # ArrayProperty of TribeAlliance Structs
        self.set('TribeAlliances', ArrayProperty(child_type='StructProperty'))
        self.set('TribeGovernment', TribeGovernment())
        # ArrayProperty of PrimalPlayerCharacterConfigStructs
        self.set('MembersConfigs', ArrayProperty(child_type='StructProperty'))
        self.set('TribeLog', ArrayProperty(child_type='StrProperty'))
        self.set('LogIndex', IntProperty())

        if stream is not None:
            while stream.peek(stream.readNullTerminatedString) != 'None':
                self.load_and_set_next_property(stream)
            stream.readNullTerminatedString()

    def _exclude(self):
        self.data['TribeGovernment']._exclude()
        zero_log_index = self.data['LogIndex'].value == 0
        empty_log = len(self.data['TribeLog'].value) == 0
        if zero_log_index or empty_log:
            self.data['LogIndex'].included = False

    def _write_to_stream(self, stream):
        self._exclude()
        self._calc_size()
        self._write_shared_struct_info(stream)
        self.data['TribeName']._write_to_stream(stream)
        self.data['OwnerPlayerDataID']._write_to_stream(stream)
        self.data['TribeID']._write_to_stream(stream)
        self.data['MembersPlayerName']._write_to_stream(stream)
        self.data['MembersPlayerDataID']._write_to_stream(stream)
        self.data['MembersRankGroups']._write_to_stream(stream)
        self.data['bSetGovernment']._write_to_stream(stream)
        self.data['TribeAdmins']._write_to_stream(stream)
        self.data['TribeAlliances']._write_to_stream(stream)
        self.data['TribeGovernment']._write_to_stream(stream)
        self.data['MembersConfigs']._write_to_stream(stream)
        self.data['TribeLog']._write_to_stream(stream)
        self.data['LogIndex']._write_to_stream(stream)
        stream.writeNullTerminatedString('None')


class TribeAlliance(BaseStruct):

    def __init__(self, stream=None):
        BaseStruct.__init__(self, stream)
        self.set('AllianceName', StrProperty())
        self.set('AllianceID', UInt32Property())
        self.set('MembersTribeName', ArrayProperty(child_type='StrPropery'))
        self.set('MembersTribeID', ArrayProperty(child_type='UInt32Property'))
        self.set('AdminsTribeID', ArrayProperty(child_type='UInt32Property'))


class TribeGovernment(BaseStruct):

    def __init__(self, stream=None):
        BaseStruct.__init__(self)
        self.set('TribeGovern_PINCode', IntProperty())
        self.set('TribeGovern_DinoOwnership', IntProperty())
        self.set('TribeGovern_StructureOwnership', IntProperty())
        self.set('TribeGovern_DinoUnclaimAdminOnly', IntProperty())

        if stream is not None:
            while stream.peek(stream.readNullTerminatedString) != 'None':
                self.load_and_set_next_property(stream)
            stream.readNullTerminatedString()

    def _exclude(self):
        self.included = False
        for key, v in self.data.iteritems():
            if v.value == 0:
                v.included = False
            else:
                self.included = True


PROPERTIES = {
    'IntProperty': IntProperty,
    'UIntProperty': UInt32Property,
    'UInt32Property': UInt32Property,
    'Int16Property': Int16Property,
    'UInt16Property': UInt16Property,
    'Int64Property': Int64Property,
    'UInt64Property': UInt64Property,
    'FloatProperty': FloatProperty,
    'DoubleProperty': DoubleProperty,
    'StrProperty': StrProperty,
    'BoolProperty': BoolProperty,
    'ArrayProperty': ArrayProperty,
    'ByteProperty': ByteProperty,
    'ObjectProperty': ObjectProperty,
}

# Long Variable PEP8 conformance
ppcsstruct = PrimalPersistentCharacterStatsStruct

STRUCTS = {
    'PrimalPlayerDataStruct': PrimalPlayerDataStruct,
    'UniqueNetIdRepl': UniqueNetIdRepl,
    'PrimalPlayerCharacterConfigStruct': PrimalPlayerCharacterConfigStruct,
    'LinearColor': LinearColor,
    'TribeData': TribeData,
    'TribeGovernment': TribeGovernment,
    'PrimalPersistentCharacterStatsStruct': ppcsstruct
}
