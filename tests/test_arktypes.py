import pytest

from context import arktypes, ark, binary


data_dir = '../data/'
output_dir = 'tests/output/'


def write_and_read(file_name, prop):
    file = output_dir + file_name
    with open(file, 'wb') as ofile:
        ostream = binary.BinaryStream(ofile)
        prop._write_to_stream(ostream)
    with open(file, 'rb') as ifile:
        istream = binary.BinaryStream(ifile)
        name, prop_type = istream.read_pair()
        prop2 = prop.__class__(stream=istream)
        prop2.var_name = name
        return prop2


class TestStrProperty:

    def test_init(self):
        prop = arktypes.StrProperty('Something')
        assert prop.value == 'Something'

    def test_size(self):
        new_value = 'One'
        prop = arktypes.StrProperty(new_value)
        size = prop._calc_inner_size()
        assert size == len(new_value) + 5

    def test_total_size(self):
        val = 'Woobles'
        prop = arktypes.StrProperty(val)
        prop.var_name = 'CharacterName'
        size = prop._calc_size()
        # Size of the Value, 4 bytes for length and 1 byte for null
        thesize = len(val) + 5
        # Size of the Variable name NTString
        thesize = thesize + len(prop.var_name) + 5
        # Size of the type NTString
        thesize = thesize + len(prop.__class__.__name__) + 5
        # Size of the two ints, size and index
        thesize = thesize + 8
        assert size == thesize

    def test_write_read(self):
        val = 'Woobles'
        prop = arktypes.StrProperty(val)
        prop.var_name = 'CharacterName'
        prop._calc_inner_size()
        prop2 = write_and_read('strproperty.output', prop)
        assert prop2.value == prop.value
        assert prop2.var_name == prop.var_name


class TestArrayProperty:

    def test_init(self):
        prop = arktypes.ArrayProperty()
        assert len(prop.value) == 0

    def test_write_read(self):
        prop = arktypes.ArrayProperty()
        prop2 = arktypes.IntProperty(value=2)
        prop2.var_name = 'Test'
        prop.var_name = 'TestArray'
        prop.value.append(prop2)
        prop._calc_size()
        prop3 = write_and_read('arrayproperty.output', prop)
        assert prop3.length == len(prop.value)
        assert prop3.value[0].value == prop2.value


class TestByteProperty:

    def test_init(self):
        prop = arktypes.ByteProperty(value=10)
        assert prop.value == 10

    def test_write_read(self):
        prop = arktypes.ByteProperty(value=3)
        prop.var_name = 'NumberOfLevelUpPointsApplied'
        prop2 = write_and_read('byteproperty.output', prop)
        assert prop2.value == prop.value
        assert prop2.var_name == prop.var_name


class TestObjectProperty:

    def test_init(self):
        prop = arktypes.ObjectProperty(value='campfire')
        assert prop.value == 'campfire'

    def test_write_read(self):
        prop = arktypes.ObjectProperty(value='campfire')
        prop.var_name = 'DefaultItemSlot'
        prop._calc_size()
        prop2 = write_and_read('objectproperty.output', prop)
        assert prop2.value == prop.value
        assert prop2.var_name == prop2.var_name


class TestFloatProperty:

    def test_init(self):
        prop = arktypes.FloatProperty(value=3)
        assert prop.value == 3.0
        assert isinstance(prop.value, float)

    def test_write_read(self):
        prop = arktypes.FloatProperty(value=0.75)
        prop.var_name = 'AFloatValue'
        prop._calc_size()
        prop2 = write_and_read('floatproperty.output', prop)
        assert prop2.value == prop.value
        assert prop2.var_name == prop.var_name


class TestDoubleProperty:

    def test_init(self):
        prop = arktypes.DoubleProperty(value=3)
        assert prop.value == 3.0
        assert isinstance(prop.value, float)

    def test_write_read(self):
        prop = arktypes.DoubleProperty(value=0.75)
        prop.var_name = 'ADoubleValue'
        prop._calc_size()
        prop2 = write_and_read('doubleproperty.output', prop)
        assert prop2.value == prop.value
        assert prop2.var_name == prop.var_name


class TestInt16Property:

    def test_init(self):
        prop = arktypes.Int16Property(value=3.0)
        assert prop.value == 3
        assert isinstance(prop.value, int)

    def test_write_read(self):
        prop = arktypes.Int16Property(value=5)
        prop.var_name = 'AnInt16Value'
        prop._calc_size()
        prop2 = write_and_read('int16property.output', prop)
        assert prop2.value == prop.value
        assert prop2.var_name == prop.var_name


class TestUInt16Property:

    def test_init(self):
        prop = arktypes.UInt16Property(value=3.0)
        assert prop.value == 3
        assert isinstance(prop.value, int)

    def test_write_read(self):
        prop = arktypes.UInt16Property(value=5)
        prop.var_name = 'AnUInt16Value'
        prop._calc_size()
        prop2 = write_and_read('uint16property.output', prop)
        assert prop2.value == prop.value
        assert prop2.var_name == prop.var_name


class TestIntProperty:

    def test_init(self):
        prop = arktypes.IntProperty(value=3.0)
        assert prop.value == 3
        assert isinstance(prop.value, int)

    def test_write_read(self):
        prop = arktypes.IntProperty(value=5)
        prop.var_name = 'AnIntValue'
        prop._calc_size()
        prop2 = write_and_read('intproperty.output', prop)
        assert prop2.value == prop.value
        assert prop2.var_name == prop.var_name


class TestUInt32Property:

    def test_init(self):
        prop = arktypes.UInt32Property(value=3.0)
        assert prop.value == 3
        assert isinstance(prop.value, int)

    def test_write_read(self):
        prop = arktypes.UInt32Property(value=5)
        prop.var_name = 'AUInt32Value'
        prop._calc_size()
        prop2 = write_and_read('uint32property.output', prop)
        assert prop2.value == prop.value
        assert prop2.var_name == prop.var_name


class TestInt64Property:

    def test_init(self):
        prop = arktypes.Int64Property(value=3.0)
        assert prop.value == 3
        assert isinstance(prop.value, int)

    def test_write_read(self):
        prop = arktypes.Int64Property(value=5)
        prop.var_name = 'AnInt64Value'
        prop._calc_size()
        prop2 = write_and_read('int64property.output', prop)
        assert prop2.value == prop.value
        assert prop2.var_name == prop.var_name


class TestUInt64Property:

    def test_init(self):
        prop = arktypes.UInt64Property(value=3.0)
        assert prop.value == 3
        assert isinstance(prop.value, int)

    def test_write_read(self):
        prop = arktypes.UInt64Property(value=5)
        prop.var_name = 'AUInt64Value'
        prop._calc_size()
        prop2 = write_and_read('uint64property.output', prop)
        assert prop2.value == prop.value
        assert prop2.var_name == prop.var_name


class TestBoolProperty:

    def test_init(self):
        prop = arktypes.BoolProperty(value=False)
        assert prop.value is False
        assert isinstance(prop.value, bool)

    def test_write_read(self):
        prop = arktypes.BoolProperty(value=True)
        prop.var_name = 'SomeBooleanValue'
        prop._calc_size()
        prop2 = write_and_read('boolproperty.output', prop)
        assert prop2.value == prop.value
        assert prop2.var_name == prop.var_name
