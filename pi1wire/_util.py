def mac_to_dirname(mac_address: str) -> str:
    return '%s-%s' % (mac_address[:2], mac_address[2:])

def dirname_to_mac(dirname: str) -> str:
    return dirname.replace('-', '')
