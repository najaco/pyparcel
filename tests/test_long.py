import unittest
from typing import List

import pyparcel
import struct
from pyparcel import Long

DATA: List[int] = [
    -2147483648,
    -2050885494,
    -2045671331,
    -1821277296,
    -1733641959,
    -1710383249,
    -1666253298,
    -1662953335,
    -1648529414,
    -1628631921,
    -1557881126,
    -1419581170,
    -1338662161,
    -1337986383,
    -1323366154,
    -1322995288,
    -1194891050,
    -1179232620,
    -1150103635,
    -1137047886,
    -1087206506,
    -1035849325,
    -1012213386,
    -1003580001,
    -959888837,
    -882604283,
    -753834715,
    -686107842,
    -647447675,
    -539691030,
    -529996608,
    -431912426,
    -431733321,
    -430847996,
    -386882016,
    -333921561,
    -251352519,
    -182451347,
    -132447078,
    -67626498,
    -13167242,
    -1,
    0,
    1,
    6580228,
    50418132,
    88433476,
    169767434,
    218744220,
    241253021,
    269720969,
    274658244,
    302176060,
    464599696,
    478084257,
    484752022,
    619149275,
    676350916,
    697416426,
    720009925,
    777142258,
    787536354,
    813138309,
    815346149,
    876982665,
    1015602221,
    1055132508,
    1086994069,
    1088495583,
    1186133728,
    1186405109,
    1207665014,
    1233410533,
    1245003777,
    1255409804,
    1267197251,
    1300837554,
    1389771123,
    1391517406,
    1434823853,
    1437753950,
    1444499038,
    1452479782,
    1467085383,
    1520100293,
    1535844506,
    1562108853,
    1608081841,
    1735628025,
    1760360519,
    1793506875,
    1841323337,
    1888982643,
    1921092813,
    1989707010,
    2037006777,
    2046862094,
    2099937592,
    2127608936,
    2147483647,
]


class TestStrictLong(unittest.TestCase):
    def test_load(self):
        for i in DATA:
            self.assertEqual(pyparcel.load(Long(i)), struct.pack("=l", i))

    def test_load_unload(self):
        for i in DATA:
            self.assertEqual(
                Long(i), pyparcel.unload(pyparcel.load(Long(i)), Long()),
            )


if __name__ == "__main__":
    unittest.main()
