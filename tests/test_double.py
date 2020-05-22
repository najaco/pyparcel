import unittest
from typing import List

import pyparcel
import struct
from pyparcel import Double

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


class TestStrictDouble(unittest.TestCase):
    def test_pack(self):
        for i in DATA:
            self.assertEqual(pyparcel.pack(Double(i)), struct.pack("=d", i))

    def test_pack_unpack(self):
        for i in DATA:
            self.assertEqual(
                Double(i), pyparcel.unpack(pyparcel.pack(Double(i)), Double()),
            )


if __name__ == "__main__":
    unittest.main()
