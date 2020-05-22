import unittest
from typing import List

import pyparcel
import struct
from pyparcel.strict_type import Short

DATA = [-32269, -32211, -29664, -29518, -28231, -27517, -26888, -26463, -25315, -25058, -24911, -24214, -23545, -23453,
        -23417, -23164, -21521, -21450, -20115, -19419, -19251, -18930, -18732, -18341, -17715, -17224, -17014, -16601,
        -16273, -14844, -14421, -14269, -13716, -12806, -12605, -12162, -11476, -10445, -10265, -9716, -9180, -8906,
        -8493, -6973, -6239, -5448, -3499, -2100, -1510, -1266, -1, 0, 1, 697, 1036, 2771, 3158, 3543, 5450, 5566, 7179,
        7308, 8117, 8477, 9345, 10612, 11669, 11701, 13188, 13977, 14409, 14445, 14575, 16119, 16232, 17499, 17815,
        18735, 18894, 19858, 20029, 22372, 22504, 22810, 24072, 24807, 24814, 25365, 25885, 25903, 26445, 26933, 27299,
        29153, 29828, 30442, 31183, 31274, 32121, 32445]


class MyTestCase(unittest.TestCase):

    def test_pack(self):
        for i in DATA:
            y = struct.pack('h', i)
            self.assertEqual(pyparcel.pack(Short(i)), y)

    def test_pack_unpack(self):
        for i in DATA:
            self.assertEqual(Short(i), pyparcel.unpack(pyparcel.pack(Short(i)), Short()))


if __name__ == '__main__':
    unittest.main()
