import struct
import unittest
from typing import List

import pyparcel

ACCURACY = 3

DATA: List[int] = [
    -12345.56789,
    -53.56,
    -30.4,
    -20.5,
    -5.7,
    -1.0,
    -0.2,
    0.0,
    0.2,
    1.0,
    5.7,
    30.4,
    53.56,
    12345.56789,
]


class MyTestCase(unittest.TestCase):
    def test_pack(self):
        for i in DATA:
            assert pyparcel.pack(i) == struct.pack("f", i)

    def test_pack_unpack(self):

        data: List[int] = [
            -12345.56789,
            -53.56,
            -30.4,
            -20.5,
            -5.7,
            -1.0,
            -0.2,
            0.0,
            0.2,
            1.0,
            5.7,
            30.4,
            53.56,
            12345.56789,
        ]
        for i in data:
            assert round(i, ACCURACY) == round(
                pyparcel.unpack(pyparcel.pack(i), float()), ACCURACY
            )


if __name__ == "__main__":
    unittest.main()
