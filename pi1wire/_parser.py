from typing import Tuple
import re
from ._exception import UnsupportResponseException

def parse_response(data: str) -> Tuple[str, str, str]:
    m = re.search(r'[0-9a-f: ]+crc=(\w{2}) (YES|NO)\n[0-9a-f ]+t=(-?\d+)', data)
    if m is None:
        raise UnsupportResponseException(f'Unsupport response [{data}]')
    crc, check, raw_value = m.groups()
    return crc, check, raw_value
