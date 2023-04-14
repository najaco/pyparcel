import unittest
from typing import List

import pyparcel
import struct
from pyparcel.strict_type import Char

DATA = [chr(i) for i in range(0, 128)]



class MyTestCase(unittest.TestCase):

    def test_pack(self):
        for i in DATA:
            self.assertEqual(pyparcel.pack(Char(i)), struct.pack('c', i.encode('ascii')))

    def test_pack_unpack(self):
        for i in DATA:
            self.assertEqual(Char(i), pyparcel.unpack(pyparcel.pack(Char(i)), Char()))


if __name__ == '__main__':
    unittest.main()
