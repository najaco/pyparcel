import unittest
from typing import List

import pyparcel
import struct
from pyparcel import UnsignedInt

DATA: List[int] = [
    0,
    1,
    10,
    57,
    124,
    70423640,
    114886406,
    177128892,
    239915431,
    284786935,
    348802156,
    404583426,
    419624996,
    511631626,
    720369325,
    727965462,
    769265286,
    879030686,
    889346346,
    899774076,
    913353185,
    931726215,
    945074270,
    1015972729,
    1020114561,
    1058308388,
    1125314019,
    1166198434,
    1205697641,
    1273539478,
    1305268329,
    1355506197,
    1473750109,
    1523412837,
    1526656344,
    1528351914,
    1602255799,
    1617550924,
    1724524649,
    1781811026,
    1810138147,
    1859680622,
    1898949502,
    1932234159,
    1985936434,
    2017058931,
    2111829921,
    2201749525,
    2246449381,
    2331625914,
    2348941408,
    2365165247,
    2414841330,
    2523476867,
    2576947575,
    2610177876,
    2663921972,
    2696627322,
    2793908058,
    2802361010,
    2816426979,
    2840527663,
    2893071034,
    2908571643,
    2952366287,
    3035345993,
    3040178514,
    3054941528,
    3079436177,
    3083694004,
    3098313365,
    3140871279,
    3192874130,
    3237445545,
    3238639675,
    3247252465,
    3266072298,
    3269137118,
    3276748951,
    3296809065,
    3307799963,
    3378457618,
    3400949074,
    3514176250,
    3520548270,
    3568257069,
    3795457186,
    3820778557,
    3898676732,
    3917388598,
    3921267257,
    3979361443,
    4120560431,
    4138752800,
    4163504170,
    4209006275,
    4219034387,
    4238459297,
    4265703226,
    4294967295,
]


class TestStrictUnsignedInt(unittest.TestCase):
    def test_pack(self):
        for i in DATA:
            self.assertEqual(pyparcel.pack(UnsignedInt(i)), struct.pack("=I", i))

    def test_pack_unpack(self):
        for i in DATA:
            self.assertEqual(
                UnsignedInt(i),
                pyparcel.unpack(pyparcel.pack(UnsignedInt(i)), UnsignedInt()),
            )


if __name__ == "__main__":
    unittest.main()
