from pi1wire import Pi1Wire, Resolution

for s in Pi1Wire().find_all_sensors():
    print(f'{s.mac_address} = {s.get_temperature():.3f}')

    s.change_resolution(Resolution.X0_5)
    print(f'{s.mac_address} = {s.get_temperature():.3f}')

    s.change_resolution(Resolution.X0_0625)
    print(f'{s.mac_address} = {s.get_temperature():.3f}')
