import os

from pi1wire._driver import W1Driver

from ._fixture import temp_dir_path


def test_read_w1_data(temp_dir_path):
    p = os.path.join(temp_dir_path, '28-000000654321')
    os.mkdir(p)
    r = '''96 01 4b 46 7f ff 0a 10 0a : crc=0a YES
96 01 4b 46 7f ff 0a 10 0a t=25375
'''
    with open(os.path.join(p, 'w1_data'), 'w', encoding='utf-8') as f:
        f.write(r)

    base_path = temp_dir_path + '/%s/w1_data'
    d = W1Driver(base_path)
    assert d.read_w1_data('28000000654321') == r
