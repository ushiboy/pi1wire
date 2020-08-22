import pytest
from pi1wire._exception import UnsupportResponseException
from pi1wire._parser import parse_response

def test_parse_response():
    r1 = '''96 01 4b 46 7f ff 0a 10 0a : crc=0a YES
96 01 4b 46 7f ff 0a 10 0a t=25375
'''
    assert parse_response(r1) == ('0a', 'YES', '25375')

    r2 = '''96 01 4b 46 7f ff 0a 10 0a : crc=0a NO
96 01 4b 46 7f ff 0a 10 0a t=25375
'''
    assert parse_response(r2) == ('0a', 'NO', '25375')

    r3 = '96 01 4b 46 7f ff 0a 10 0a : crc=0a YES'
    with pytest.raises(UnsupportResponseException):
        parse_response(r3)
