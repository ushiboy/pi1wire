class InvalidCRCException(Exception):
    '''
    Invalid CRC
    '''


class NotFoundSensorException(Exception):
    '''
    Sensor Not found
    '''


class UnsupportResponseException(Exception):
    '''
    Unsupport Response
    '''


class FailedToChangeResolutionException(Exception):
    '''
    Failed to change resolution
    '''
