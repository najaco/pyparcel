import unittest
from typing import List

import pyparcel
import struct
from pyparcel.strict_type import SignedChar

DATA = range(0, 128)


class TestStrictSignedShort(unittest.TestCase):
    def test_load(self):
        for i in DATA:
            y = struct.pack("=b", i)
            self.assertEqual(pyparcel.load(SignedChar(i)), y)

    def test_load_unload(self):
        for i in DATA:
            self.assertEqual(
                SignedChar(i),
                pyparcel.unload(pyparcel.load(SignedChar(i)), SignedChar()),
            )


if __name__ == "__main__":
    unittest.main()
