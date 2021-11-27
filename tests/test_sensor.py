from typing import List
import pytest
from pi1wire._driver import W1DriverInterface
from pi1wire._exception import InvalidCRCException
from pi1wire._sensor import OneWire

RAW_VALUE = '''b8 01 4b 46 7f ff 08 10 8a : crc=8a YES
b8 01 4b 46 7f ff 08 10 8a t=27500
'''

INVALID_RAW_VALUE = '''b8 01 4b 46 7f ff 08 10 8a : crc=00 NO
b8 01 4b 46 7f ff 08 10 8a t=27500
'''

POWER_ON_RESET_VALUE = '''50 05 4b 46 7f ff 0c 10 1c : crc=1c YES
50 05 4b 46 7f ff 0c 10 1c t=85000
'''

class DummyDriver(W1DriverInterface):

    def read_w1_data(self, mac_address: str) -> str:
        return RAW_VALUE

class InvalidDriver(W1DriverInterface):

    def read_w1_data(self, mac_address: str) -> str:
        return INVALID_RAW_VALUE

class PowerOnResetValueDriver(W1DriverInterface):

    def __init__(self, values: List[str]):
        self._values = values

    def read_w1_data(self, mac_address: str) -> str:
        return self._values.pop(0)

def test_get_temperature():
    assert OneWire('abcd', DummyDriver()).get_temperature() == 27.5

    with pytest.raises(InvalidCRCException):
        OneWire('abcd', InvalidDriver()).get_temperature()

    # case 85000
    assert OneWire('abcd', PowerOnResetValueDriver([
            POWER_ON_RESET_VALUE,
            POWER_ON_RESET_VALUE
        ])).get_temperature() == 85.0

    # case power on reset value
    assert OneWire('abcd', PowerOnResetValueDriver([
            POWER_ON_RESET_VALUE,
            RAW_VALUE
        ])).get_temperature() == 27.5

    # case power on reset value -> invalid -> power on reset value -> valid value
    w1 = OneWire('abcd', PowerOnResetValueDriver([
            POWER_ON_RESET_VALUE,
            INVALID_RAW_VALUE,
            POWER_ON_RESET_VALUE,
            RAW_VALUE
        ]))
    with pytest.raises(InvalidCRCException):
        w1.get_temperature()
    assert w1.get_temperature() == 27.5

    # case power on reset value -> invalid -> 85000
    w2 = OneWire('abcd', PowerOnResetValueDriver([
            POWER_ON_RESET_VALUE,
            INVALID_RAW_VALUE,
            POWER_ON_RESET_VALUE,
            POWER_ON_RESET_VALUE
        ]))
    with pytest.raises(InvalidCRCException):
        w2.get_temperature()
    assert w2.get_temperature() == 85.0

    # case power on reset value -> invalid -> valid value
    w3 = OneWire('abcd', PowerOnResetValueDriver([
            POWER_ON_RESET_VALUE,
            INVALID_RAW_VALUE,
            RAW_VALUE
        ]))
    with pytest.raises(InvalidCRCException):
        w3.get_temperature()
    assert w3.get_temperature() == 27.5
