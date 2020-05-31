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
    def test_same_load(self):
        for i in DATA:
            self.assertEqual(pyparcel.load(*i), struct.pack("=" + ("i" * len(i)), *i))

    def test_same_load_unload(self):
        for i in DATA:
            self.assertEqual(i, pyparcel.unload(pyparcel.load(i), *[int()] * len(i)))

    def test_diff_load_unload(self):
        data = pyparcel.load(1, 2, 3.5)
        self.assertEqual((1, 2, 3.5), pyparcel.unload(data, int(), int(), float()))


if __name__ == "__main__":
    unittest.main()
