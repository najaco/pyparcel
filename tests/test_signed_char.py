import unittest
from typing import List

import pyparcel
import struct
from pyparcel.strict_type import SignedChar

DATA = range(0, 128)


class TestStrictSignedShort(unittest.TestCase):
    def test_pack(self):
        for i in DATA:
            y = struct.pack("=b", i)
            self.assertEqual(pyparcel.pack(SignedChar(i)), y)

    def test_pack_unpack(self):
        for i in DATA:
            self.assertEqual(
                SignedChar(i),
                pyparcel.unpack(pyparcel.pack(SignedChar(i)), SignedChar()),
            )


if __name__ == "__main__":
    unittest.main()
