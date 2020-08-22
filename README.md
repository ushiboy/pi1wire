pi1wire
=====

## Quick Sample

```python
from pi1wire import Pi1Wire

for s in Pi1Wire().find_all_sensors():
    print('%s = %.2f' % (s.mac_address, s.get_temperature()))
```

## API

### Pi1Wire

#### `find_all_sensors() -> List[OneWire]`

#### `find(mac_address: str) -> OneWire`

### OneWire

#### `mac_address`

#### `get_temperature() -> float`

## Change Log

### 0.1.0

Initial release.

## License

MIT
