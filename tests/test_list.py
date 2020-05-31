import unittest
from typing import List, TypeVar

import pyparcel
import struct
from pyparcel import Long, Int, LongLong, UnsignedShort


class TestList(unittest.TestCase):
    def test_load_1(self):
        data = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.assertEqual(
            pyparcel.load(data),
            struct.pack("=i", len(data)) + struct.pack("=" + "i" * len(data), *data),
        )

    def test_load_unload_1(self):
        data = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.assertEqual(data, pyparcel.unload(pyparcel.load(data), [int()]))

    def test_inconsistent_types_raises_exception(self):
        data = [
            [0, 1.0],
            [5, 7.6],
            [5, Long(42), LongLong(132), UnsignedShort(42)],
            [43, "Hello", "World"],
        ]
        for d in data:
            self.assertRaises(Exception, pyparcel.load, d)

    def test_list_conform_does_not_raise_exception(self):
        data = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [Long(53), 13],
            [Long(53), 13, 43, Long(23)],
            [Long(53), 13, Long(43), 23],
            [53, Long(13), Long(43), 23],
            [True, False, True],
        ]
        for d in data:
            try:
                pyparcel.load(d)
            except Exception:
                self.fail(f"pyparcel.load({d}) raised Exception unexpectedly.")


if __name__ == "__main__":
    unittest.main()
