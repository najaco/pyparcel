import unittest
from typing import List

import pyparcel
import struct
from pyparcel.strict_type import UnsignedChar

DATA = range(0, 128)


class TestStrictUnsignedChar(unittest.TestCase):
    def test_load(self):
        for i in DATA:
            y = struct.pack("=B", i)
            self.assertEqual(pyparcel.load(UnsignedChar(i)), y)

    def test_load_unload(self):
        for i in DATA:
            self.assertEqual(
                UnsignedChar(i),
                pyparcel.unload(pyparcel.load(UnsignedChar(i)), UnsignedChar()),
            )


if __name__ == "__main__":
    unittest.main()
