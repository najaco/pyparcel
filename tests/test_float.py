import struct
import unittest
from typing import List
from tests.config import FLOATING_POINT_ACCURACY

import pyparcel
from pyparcel import Float


DATA: List[int] = [
    -12345.56789,
    -53.56,
    -30.4,
    -20.5,
    -5.7,
    -1.0,
    -0.2,
    0.0,
    0.2,
    1.0,
    5.7,
    30.4,
    53.56,
    12345.56789,
]


class TestDefaultFloat(unittest.TestCase):
    def test_pack(self):
        for i in DATA:
            assert pyparcel.pack(i) == struct.pack("=f", i)

    def test_pack_unpack(self):
        for i in DATA:
            self.assertEqual(
                round(i, FLOATING_POINT_ACCURACY),
                round(
                    pyparcel.unpack(pyparcel.pack(i), float()), FLOATING_POINT_ACCURACY
                ),
            )


class TestStrictFloat(unittest.TestCase):
    def test_pack(self):
        for i in DATA:
            assert pyparcel.pack(Float(i)) == struct.pack("=f", i)

    def test_pack_unpack(self):
        for i in DATA:
            self.assertEqual(
                round(Float(i), FLOATING_POINT_ACCURACY),
                round(
                    pyparcel.unpack(pyparcel.pack(Float(i)), Float()),
                    FLOATING_POINT_ACCURACY,
                ),
            )


class TestDefaultMatchesStrict(unittest.TestCase):
    def test_pack(self):
        for i in DATA:
            assert pyparcel.pack(Float(i)) == pyparcel.pack(i)

    def test_pack_unpack(self):
        for i in DATA:
            self.assertEqual(
                round(
                    pyparcel.unpack(pyparcel.pack(i), float()), FLOATING_POINT_ACCURACY
                ),
                round(
                    pyparcel.unpack(pyparcel.pack(Float(i)), Float()),
                    FLOATING_POINT_ACCURACY,
                ),
            )


if __name__ == "__main__":
    unittest.main()
