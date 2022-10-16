from subprocess import CalledProcessError, run

from ._constant import Resolution
from ._exception import FailedToChangeResolutionException
from ._util import mac_to_dirname


class W1DriverInterface:

    def read_w1_data(self, mac_address: str) -> str:
        raise NotImplementedError

    def change_w1_resolution(self, mac_address: str, resolution: Resolution, use_sudo: bool = True):
        raise NotImplementedError


class W1Driver(W1DriverInterface):

    def __init__(self, base_path: str, subprocess_run=run):
        self._base_path = base_path
        self._run = subprocess_run

    def read_w1_data(self, mac_address: str) -> str:
        p = self._base_path % mac_to_dirname(mac_address)
        with open(p, encoding='utf-8') as f:
            return f.read()

    def change_w1_resolution(self, mac_address: str, resolution: Resolution, use_sudo: bool = True):
        p = self._base_path % mac_to_dirname(mac_address)
        c = ['sudo', 'sh', '-c', f'echo {resolution.value} > {p}']
        cmd = c if use_sudo else c[1:]
        try:
            self._run(cmd, check=True)
        except CalledProcessError as e:
            raise FailedToChangeResolutionException(
                f'Failed to change resolution [resolution:{resolution.value}]') from e
