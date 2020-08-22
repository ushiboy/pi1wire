from pi1wire._util import mac_to_dirname, dirname_to_mac

def test_mac_to_dirname():
    assert mac_to_dirname('2800000b1b37fc') == '28-00000b1b37fc'

def test_dirname_to_mac():
    assert dirname_to_mac('28-00000b1b37fc') == '2800000b1b37fc'
