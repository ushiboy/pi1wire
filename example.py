from pi1wire import Pi1Wire

for s in Pi1Wire().find_all_sensors():
    print('%s = %.2f' % (s.mac_address, s.get_temperature()))
