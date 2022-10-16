import os
from subprocess import CalledProcessError

import pytest

from pi1wire._constant import Resolution
from pi1wire._driver import W1Driver
from pi1wire._exception import FailedToChangeResolutionException
from pi1wire._util import mac_to_dirname

from ._fixture import temp_dir_path


class DummySubprocessRunner:

    @property
    def passed_args(self):
        return self._args

    def __init__(self, return_code=0, stderr=b''):
        self._args = None
        self._return_code = return_code
        self._stderr = stderr

    def __call__(self, args, check):
        self._args = args
        if self._return_code != 0:
            raise CalledProcessError(
                self._return_code, args, stderr=self._stderr)


def test_read_w1_data(temp_dir_path):
    p = os.path.join(temp_dir_path, '28-000000654321')
    os.mkdir(p)
    r = '''96 01 4b 46 7f ff 0a 10 0a : crc=0a YES
96 01 4b 46 7f ff 0a 10 0a t=25375
'''
    with open(os.path.join(p, 'w1_data'), 'w', encoding='utf-8') as f:
        f.write(r)

    base_path = temp_dir_path + '/%s/w1_data'
    d = W1Driver(base_path)
    assert d.read_w1_data('28000000654321') == r


def test_change_w1_resolution(temp_dir_path):
    run = DummySubprocessRunner()

    base_path = temp_dir_path + '/%s/w1_data'
    mac_address = '28000000654321'
    p = base_path % mac_to_dirname(mac_address)
    d = W1Driver(base_path, run)

    d.change_w1_resolution(mac_address, Resolution.X0_5)
    assert run.passed_args == ['sudo', 'sh', '-c', f'echo 9 > {p}']

    d.change_w1_resolution(mac_address, Resolution.X0_25)
    assert run.passed_args == ['sudo', 'sh', '-c', f'echo 10 > {p}']

    d.change_w1_resolution(mac_address, Resolution.X0_125)
    assert run.passed_args == ['sudo', 'sh', '-c', f'echo 11 > {p}']

    d.change_w1_resolution(mac_address, Resolution.X0_0625)
    assert run.passed_args == ['sudo', 'sh', '-c', f'echo 12 > {p}']

    d.change_w1_resolution(mac_address, Resolution.X0_5, False)
    assert run.passed_args == ['sh', '-c', f'echo 9 > {p}']


def test_change_w1_resolution_when_failed(temp_dir_path):
    run = DummySubprocessRunner(2, 'Permission denied')

    base_path = temp_dir_path + '/%s/w1_data'
    mac_address = '28000000654321'
    d = W1Driver(base_path, run)

    with pytest.raises(FailedToChangeResolutionException) as e:
        d.change_w1_resolution(mac_address, Resolution.X0_5)

    assert str(e.value) == 'Failed to change resolution [resolution:9]'
