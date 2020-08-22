import glob
import os
from typing import List
from ._driver import W1Driver
from ._exception import NotFoundSensorException
from ._sensor import OneWireInterface, OneWire
from ._util import dirname_to_mac, mac_to_dirname


class Pi1WireInterface:

    def find_all_sensors(self) -> List[OneWireInterface]:
        raise NotImplementedError

    def find(self, mac_address: str) -> OneWireInterface:
        raise NotImplementedError

class Pi1Wire(Pi1WireInterface):

    def __init__(self, base_path: str = '/sys/bus/w1/devices'):
        self._base_path = base_path
        self._driver = W1Driver(base_path + '/%s/w1_slave')

    def find_all_sensors(self) -> List[OneWireInterface]:
        sensors: List[OneWireInterface] = []
        for p in glob.glob(self._base_path + '/*-*'):
            mac = dirname_to_mac(os.path.basename(p))
            sensors.append(OneWire(mac, self._driver))
        return sensors

    def find(self, mac_address: str) -> OneWireInterface:
        p = os.path.join(self._base_path, mac_to_dirname(mac_address))
        if not os.path.exists(p):
            raise NotFoundSensorException('Not found sensor [%s]' % mac_address)
        return OneWire(mac_address, self._driver)
