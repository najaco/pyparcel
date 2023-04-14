import unittest
from typing import List, TypeVar

import pyparcel
import struct
from pyparcel import Long, Int


class TestList(unittest.TestCase):
    def test_pack_1(self):
        data = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.assertEqual(pyparcel.pack(data), struct.pack("=i", len(data)) + struct.pack("=" + "i" * len(data), *data))

    def test_pack_unpack_1(self):
        data = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.assertEqual(data, pyparcel.unpack(pyparcel.pack(data), [int()]))

    def test_inconsistent_types_raises_exception(self):
        data = [
            [0, 1.0],
            [5, 7.6],
            ]
        for d in data:
            self.assertRaises(Exception, pyparcel.pack, d)

    def test_inconsistent_but_same_types_does_not_raise_exception(self):
        data = [
            [0, 1.0],
            [5, 7.6],
        ]

if __name__ == "__main__":
    unittest.main()
