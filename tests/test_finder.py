import os

import pytest

from pi1wire._constant import Resolution
from pi1wire._driver import W1DriverInterface
from pi1wire._exception import NotFoundSensorException
from pi1wire._finder import Pi1Wire

from ._fixture import temp_dir_path


class DummyDriver(W1DriverInterface):

    @property
    def passed_parameters(self):
        return self._parameters

    def __init__(self):
        self._parameters = []

    def read_w1_data(self, mac_address: str) -> str:
        raise NotImplementedError

    def change_w1_resolution(self, mac_address: str, resolution: Resolution, use_sudo: bool = True):
        self._parameters.append((mac_address, resolution, use_sudo))


def test_find_all_sensors(temp_dir_path):
    os.mkdir(os.path.join(temp_dir_path, '28-000000654321'))
    os.mkdir(os.path.join(temp_dir_path, '28-000000987654'))

    p = Pi1Wire(base_path=temp_dir_path)
    r = p.find_all_sensors()
    assert len(r) == 2
    assert r[0].mac_address == '28000000654321'
    assert r[1].mac_address == '28000000987654'


def test_find(temp_dir_path):
    os.mkdir(os.path.join(temp_dir_path, '28-000000654321'))
    os.mkdir(os.path.join(temp_dir_path, '28-000000987654'))

    p = Pi1Wire(base_path=temp_dir_path)
    assert p.find('28000000654321').mac_address == '28000000654321'

    with pytest.raises(NotFoundSensorException):
        p.find('28000000000000')


def test_find_all_and_change_resolution(temp_dir_path):
    os.mkdir(os.path.join(temp_dir_path, '28-000000654321'))
    os.mkdir(os.path.join(temp_dir_path, '28-000000987654'))

    d = DummyDriver()
    p = Pi1Wire(base_path=temp_dir_path, driver=d)
    r = p.find_all_and_change_resolution(Resolution.X0_5)
    assert len(r) == 2
    assert r[0].mac_address == '28000000654321'
    assert r[1].mac_address == '28000000987654'
    assert d.passed_parameters == [
        ('28000000654321', Resolution.X0_5, True),
        ('28000000987654', Resolution.X0_5, True)
    ]

    r = p.find_all_and_change_resolution(Resolution.X0_25, False)
    assert len(r) == 2
    assert r[0].mac_address == '28000000654321'
    assert r[1].mac_address == '28000000987654'
    assert d.passed_parameters == [
        ('28000000654321', Resolution.X0_5, True),
        ('28000000987654', Resolution.X0_5, True),
        ('28000000654321', Resolution.X0_25, False),
        ('28000000987654', Resolution.X0_25, False)
    ]
