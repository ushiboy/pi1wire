from ._driver import W1DriverInterface
from ._exception import InvalidCRCException
from ._parser import parse_response

class OneWireInterface:

    _mac_address: str

    @property
    def mac_address(self) -> str:
        return self._mac_address

    def get_temperature(self) -> float:
        raise NotImplementedError

class OneWire(OneWireInterface):

    def __init__(self, mac_address: str, driver: W1DriverInterface):
        self._mac_address = mac_address
        self._driver = driver

    def get_temperature(self) -> float:
        r = self._driver.read_w1_data(self._mac_address)
        crc, check, raw_value = parse_response(r)
        if check != 'YES':
            raise InvalidCRCException('Invalid CRC [%s]' % crc)
        return int(raw_value) / 1000.0
