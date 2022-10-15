import os

import pytest

from pi1wire._exception import NotFoundSensorException
from pi1wire._finder import Pi1Wire

from ._fixture import temp_dir_path


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
