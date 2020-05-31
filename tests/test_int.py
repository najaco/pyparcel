import struct
import unittest
from typing import List

import pyparcel
from pyparcel import Int

DATA: List[int] = [
    -2147483648,
    -2131487479,
    -2083361717,
    -2071578602,
    -1997171616,
    -1959009730,
    -1858712818,
    -1853066169,
    -1807900287,
    -1681783261,
    -1678671123,
    -1659202014,
    -1635303196,
    -1635176332,
    -1597098480,
    -1552859530,
    -1520938410,
    -1342625064,
    -1311745364,
    -1299621514,
    -1292565450,
    -1282189044,
    -1142333985,
    -1113572859,
    -1113099584,
    -1088251971,
    -1053617926,
    -1009597170,
    -892485218,
    -873281755,
    -768302599,
    -735583006,
    -666710988,
    -568859086,
    -520810573,
    -491805530,
    -474702114,
    -407338878,
    -348197305,
    -341279631,
    -339039851,
    -283845951,
    -231722885,
    -223988548,
    -124038011,
    -110993442,
    -28027710,
    -1541322,
    -1000,
    -57,
    -26,
    -20,
    -5,
    -2,
    -1,
    0,
    1,
    2,
    5,
    20,
    57,
    1000,
    62714468,
    86922272,
    142039477,
    172861576,
    205630353,
    209020905,
    245410744,
    249705205,
    291475254,
    333016086,
    434135467,
    461843460,
    536800786,
    546117668,
    581742384,
    596687259,
    672585429,
    678901176,
    692017564,
    733453071,
    771256268,
    827784919,
    880274105,
    979203050,
    1142113385,
    1143510441,
    1174205727,
    1196946039,
    1302992056,
    1311835862,
    1376740506,
    1439396181,
    1485642740,
    1524374634,
    1548392468,
    1619044116,
    1642141203,
    1699898156,
    1726572483,
    1798943311,
    1824212440,
    1867378212,
    1893270666,
    1911292841,
    1966050070,
    1987138362,
    2016364412,
    2134584527,
    2147483647,
]


class TestDefaultInt(unittest.TestCase):
    def test_load(self):
        for i in DATA:
            self.assertEqual(pyparcel.load(i), struct.pack("=i", i))

    def test_load_unload(self):
        for i in DATA:
            self.assertEqual(i, pyparcel.unload(pyparcel.load(i), int()))


class TestStrictInt(unittest.TestCase):
    def test_load(self):
        for i in DATA:
            self.assertEqual(pyparcel.load(Int(i)), struct.pack("=i", i))

    def test_load_unload(self):
        for i in DATA:
            self.assertEqual(Int(i), pyparcel.unload(pyparcel.load(Int(i)), Int()))


class TestDefaultMatchesStrict(unittest.TestCase):
    def test_load(self):
        for i in DATA:
            self.assertEqual(pyparcel.load(i), pyparcel.load(Int(i)))

    def test_load_unload(self):
        for i in DATA:
            self.assertEqual(
                pyparcel.unload(pyparcel.load(i), int()),
                pyparcel.unload(pyparcel.load(Int(i)), Int()),
            )


if __name__ == "__main__":
    unittest.main()
