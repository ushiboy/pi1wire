from pi1wire._util import dirname_to_mac, mac_to_dirname


def test_mac_to_dirname():
    assert mac_to_dirname('2800000b1b37fc') == '28-00000b1b37fc'


def test_dirname_to_mac():
    assert dirname_to_mac('28-00000b1b37fc') == '2800000b1b37fc'
