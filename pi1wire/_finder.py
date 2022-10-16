import glob
import os
from typing import List

from ._constant import Resolution
from ._driver import W1Driver, W1DriverInterface
from ._exception import NotFoundSensorException
from ._sensor import OneWire, OneWireInterface
from ._util import dirname_to_mac, mac_to_dirname


class Pi1WireInterface:

    def find_all_sensors(self) -> List[OneWireInterface]:
        raise NotImplementedError

    def find(self, mac_address: str) -> OneWireInterface:
        raise NotImplementedError

    def find_all_and_change_resolution(self,
                                       resolution: Resolution,
                                       use_sudo: bool = True) -> List[OneWireInterface]:
        raise NotImplementedError


class Pi1Wire(Pi1WireInterface):

    def __init__(self, base_path: str = '/sys/bus/w1/devices', driver: W1DriverInterface = None):
        self._base_path = base_path
        self._driver = W1Driver(
            base_path + '/%s/w1_slave') if driver is None else driver

    def find_all_sensors(self) -> List[OneWireInterface]:
        sensors: List[OneWireInterface] = []
        for p in sorted(glob.glob(self._base_path + '/*-*')):
            mac = dirname_to_mac(os.path.basename(p))
            sensors.append(OneWire(mac, self._driver))
        return sensors

    def find(self, mac_address: str) -> OneWireInterface:
        p = os.path.join(self._base_path, mac_to_dirname(mac_address))
        if not os.path.exists(p):
            raise NotFoundSensorException(f'Not found sensor [{mac_address}]')
        return OneWire(mac_address, self._driver)

    def find_all_and_change_resolution(self,
                                       resolution: Resolution,
                                       use_sudo: bool = True) -> List[OneWireInterface]:
        sensors = self.find_all_sensors()
        for s in sensors:
            s.change_resolution(resolution, use_sudo)
        return sensors
