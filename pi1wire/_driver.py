from ._util import mac_to_dirname

class W1DriverInterface:

    def read_w1_data(self, mac_address: str) -> str:
        raise NotImplementedError

class W1Driver(W1DriverInterface):

    def __init__(self, base_path: str):
        self._base_path = base_path

    def read_w1_data(self, mac_address: str) -> str:
        p = self._base_path % mac_to_dirname(mac_address)
        with open(p, encoding='utf-8') as f:
            return f.read()
