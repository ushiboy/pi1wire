from pi1wire._driver import W1DriverInterface
from pi1wire._sensor import OneWire

RAW_VALUE = '''b8 01 4b 46 7f ff 08 10 8a : crc=8a YES
b8 01 4b 46 7f ff 08 10 8a t=27500
'''

class DummyDriver(W1DriverInterface):

    def read_w1_data(self, mac_address: str) -> str:
        return RAW_VALUE


def test_get_temperature():
    s = OneWire('abcd', DummyDriver())
    assert s.get_temperature() == 27.5
