from enum import Enum, unique


@unique
class Resolution(Enum):
    # 0.5 deg C
    X0_5 = 9
    # 0.25 deg C
    X0_25 = 10
    # 0.125 deg C
    X0_125 = 11
    # 0.0625 deg C (default)
    X0_0625 = 12
