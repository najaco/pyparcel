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


class TestTuple(unittest.TestCase):
    def test_pack(self):
        for i in DATA:
            self.assertEqual(pyparcel.pack(i), struct.pack("i" * len(i), *i))

    def test_pack_unpack(self):
        for i in DATA:
            self.assertEqual(
                i, pyparcel.unpack(pyparcel.pack(i), tuple([int()] * len(i)))
            )

    def test_tuple_of_tuple_pack_unpack(self):
        structure = tuple(
            [tuple([int()] * i) for i in range(len(DATA[0]), len(DATA[-1]) + 1)]
        )
        self.assertEqual(
            tuple(DATA), pyparcel.unpack(pyparcel.pack(tuple(DATA)), structure)
        )

    def simple_test(self):
        self.assertEqual(
            tuple(1, 2, 3),
            pyparcel.unpack(pyparcel.pack(tuple(1, 2, 3)), tuple(int(), int(), int())),
        )


if __name__ == "__main__":
    unittest.main()
