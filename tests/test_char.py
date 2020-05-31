import unittest
from typing import List

import pyparcel
import struct
from pyparcel.strict_type import Char

DATA = [chr(i) for i in range(0, 128)]


class TestStrictChar(unittest.TestCase):
    def test_load(self):
        for i in DATA:
            self.assertEqual(
                pyparcel.load(Char(i)), struct.pack("=c", i.encode("ascii"))
            )

    def test_load_unload(self):
        for i in DATA:
            self.assertEqual(Char(i), pyparcel.unload(pyparcel.load(Char(i)), Char()))


if __name__ == "__main__":
    unittest.main()
