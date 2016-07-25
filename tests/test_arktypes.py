from context import arktypes, ark, binary


data_dir = '../data/'
output_dir = 'tests/output/'

# @pytest.fixture(scope='session', autouse=True)
# def setup_tmpdir():
#   # If .tmp exists, delete it
#   # Create .tmp


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
    file = output_dir + 'strproperty.output'
    val = 'Woobles'
    prop = arktypes.StrProperty(val)
    prop.var_name = 'CharacterName'
    prop._calc_inner_size()
    with open(file, 'wb') as ofile:
      ostream = binary.BinaryStream(ofile)
      prop._write_to_stream(ostream)
    with open(file, 'rb') as ifile:
      istream = binary.BinaryStream(ifile)
      name, prop_type = istream.read_pair()
      secondProp = arktypes.StrProperty(stream=istream)
      secondProp.var_name = name
      assert secondProp.value == prop.value

