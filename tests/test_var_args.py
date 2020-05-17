import struct
import unittest
from typing import List

import pyparcel

DATA = []


class MyTestCase(unittest.TestCase):
    def test_pack(self):
        for i in DATA:
            self.assertEqual(pyparcel.pack(i), struct.pack("i", i))

    def test_pack_unpack(self):
        for i in DATA:
            self.assertEqual(i, pyparcel.unpack(pyparcel.pack(i), int()))


if __name__ == "__main__":
    unittest.main()
