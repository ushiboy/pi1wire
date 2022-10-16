pi1wire
=====

pi1wire is a library for the Raspberry PI 1Wire sensor.

## Quick Sample

Here is a simple usecase.

```python
from pi1wire import Pi1Wire

for s in Pi1Wire().find_all_sensors():
    print('%s = %.2f' % (s.mac_address, s.get_temperature()))
```

## OS Environment

(For Raspbian OS) Enable 1wire in raspi-config.

```
$ sudo raspi-config nonint do_onewire 0
```

## API

### Pi1Wire

This is a class that looks for sensors.

#### `find_all_sensors() -> List[OneWire]`

Get a list of OneWire instances.

#### `find(mac_address: str) -> OneWire`

Get a OneWire instance of the specified MAC address.

#### `find_all_and_change_resolution(resolution: Resolution, use_sudo: bool = True) -> List[OneWire]`

Change the resolution of all sensors found and get them as a list of OneWire instances.

### OneWire

This class controls the sensors.

#### `mac_address`

The MAC address property of the sensor.

#### `get_temperature() -> float`

Get the temperature.

#### `change_resolution(resolution: Resolution, use_sudo: bool = True) -> None`

Change the resolution of the temperature sensor.

Depending on the `Resolution` definition, change to a resolution equivalent to increments of 0.5°C, 0.25°C, 0.125°C, or 0.0625°C.

### Resolution

An enumeration that defines the resolution setting values.

#### `X0_5`

Resolution is set at 0.5°C.

#### `X0_25`

Resolution is set at 0.25°C.

#### `X0_125`

Resolution is set at 0.125°C.

#### `X0_0625`

Resolution is set at 0.0625°C.

## Change Log

### 0.3.0

- Added function to change resolution.
- Fixed so that the order of sensor detection does not change depending on the file system.

### 0.2.0

- Added check for PowerOnResetValue.

### 0.1.0

- Initial release.

## License

MIT
