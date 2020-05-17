import struct
import unittest
from typing import List

import pyparcel

DATA: List[int] = [
    -1 << 31,
    -1000,
    -57,
    -26,
    -20,
    -5,
    -2,
    -1,
    0,
    1,
    2,
    5,
    20,
    57,
    1000,
    (1 << 31) - 1,
]


class MyTestCase(unittest.TestCase):
    def test_pack(self):
        for i in DATA:
            assert pyparcel.pack(i) == struct.pack("i", i)

    def test_pack_unpack(self):
        for i in DATA:
            assert i == pyparcel.unpack(pyparcel.pack(i), int())

    def test_pack_unpack_8(self):
        for i in DATA:
            assert i == pyparcel.unpack(pyparcel.pack(i, 8), int(), 8)


if __name__ == "__main__":
    unittest.main()
