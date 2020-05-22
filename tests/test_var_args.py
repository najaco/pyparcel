import struct
import unittest

import pyparcel

DATA = [
    (1, 2),
    (1, 2, 3),
    (1, 2, 3, 4),
    (1, 2, 3, 4, 5),
    (1, 2, 3, 4, 5, 6),
    (1, 2, 3, 4, 5, 6, 7),
    (1, 2, 3, 4, 5, 6, 7, 8),
    (1, 2, 3, 4, 5, 6, 7, 8, 9),
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
]


class TestVarArgs(unittest.TestCase):
    def test_same_pack(self):
        for i in DATA:
            self.assertEqual(pyparcel.pack(*i), struct.pack("=i" * len(i), *i))

    def test_same_pack_unpack(self):
        for i in DATA:
            self.assertEqual(i, pyparcel.unpack(pyparcel.pack(i), *[int()] * len(i)))

    def test_diff_pack_unpack(self):
        data = pyparcel.pack(1, 2, 3.5)
        self.assertEqual((1, 2, 3.5), pyparcel.unpack(data, int(), int(), float()))


if __name__ == "__main__":
    unittest.main()
