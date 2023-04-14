import unittest
from typing import List

import pyparcel
import struct
from pyparcel import Short

DATA: List[int] = [
    -32768,
    -32665,
    -32547,
    -32151,
    -31558,
    -30914,
    -29412,
    -27902,
    -26817,
    -25959,
    -25472,
    -22961,
    -20778,
    -20722,
    -20356,
    -19758,
    -19438,
    -19335,
    -19255,
    -19186,
    -16781,
    -16552,
    -16242,
    -16196,
    -15771,
    -15359,
    -15292,
    -15291,
    -14762,
    -14285,
    -14206,
    -14196,
    -13593,
    -11625,
    -11318,
    -11138,
    -10796,
    -10144,
    -9986,
    -8267,
    -7962,
    -7636,
    -6771,
    -6516,
    -6438,
    -6054,
    -5304,
    -5216,
    -3916,
    -3673,
    -3618,
    -801,
    -1,
    0,
    1,
    1633,
    2002,
    2237,
    2565,
    2659,
    2679,
    3950,
    4014,
    5461,
    5697,
    6246,
    6927,
    7152,
    7463,
    7568,
    8238,
    8607,
    8864,
    12404,
    13207,
    13441,
    13763,
    18310,
    18716,
    19196,
    19452,
    20937,
    21464,
    21497,
    22046,
    22899,
    23624,
    25776,
    26786,
    27447,
    28408,
    29205,
    29253,
    29895,
    30216,
    30260,
    30696,
    32142,
    32540,
    32767,
]


class TestStrictShort(unittest.TestCase):
    def test_load(self):
        for i in DATA:
            self.assertEqual(pyparcel.load(Short(i)), struct.pack("=h", i))

    def test_load_unload(self):
        for i in DATA:
            self.assertEqual(
                Short(i), pyparcel.unload(pyparcel.load(Short(i)), Short())
            )


if __name__ == "__main__":
    unittest.main()
