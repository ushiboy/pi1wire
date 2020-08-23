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

### OneWire

This class controls the sensors.

#### `mac_address`

The MAC address property of the sensor.

#### `get_temperature() -> float`

Get the temperature.

## Change Log

### 0.1.0

Initial release.

## License

MIT
