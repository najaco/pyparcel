import unittest
from typing import List

import pyparcel
import struct
from pyparcel import UnsignedLongLong

DATA: List[int] = [
    0,
    1,
    502154864505658071,
    642935589745106987,
    754982185488431587,
    1142714022685667946,
    1386392617442585057,
    1423728044233635894,
    1432121453560921269,
    1525280000063519267,
    2012937015976617487,
    2271657469237515571,
    2470588719812926971,
    2502224967087087769,
    2558916320180623439,
    2733482941447426157,
    3278216617060465303,
    3538881715555506758,
    3902183515856343818,
    3915750604008959835,
    3945365889447251050,
    4032217908710780690,
    4430535615791550991,
    4708527573454836471,
    4731158082514761936,
    4734091444502151453,
    4892896764725735721,
    5225982249733186080,
    5281999191173686419,
    5302066624115947878,
    5531366297994851707,
    5601081712456430430,
    5622231602495539071,
    5820524174327915991,
    6392228015520535820,
    6470383424976998947,
    6546518773327043722,
    6784414100042419548,
    7064635504259883573,
    7180990876735587522,
    7192367663754906705,
    7220691498683853424,
    7258688279306462679,
    7304613714556977877,
    7323810719359440797,
    7848136306746402678,
    8037487505269529154,
    8115181825650941126,
    8284422606489779438,
    8471269998869800025,
    8510715826924816813,
    8895079095997073083,
    9018681201018028204,
    9187339780291188285,
    9574942321640094324,
    9601742288480907092,
    9847730086009946743,
    9913402890491707271,
    10597001814782449750,
    10621598205007362993,
    11159579522771543607,
    11273136702269017793,
    11414345027914404301,
    11909009570132679601,
    11926628807936265655,
    11939785720429776394,
    12156962638696695830,
    12435767766903076409,
    12619411286444285870,
    12685706754565396704,
    12831651195290374274,
    13033630506333432354,
    13277154659096345863,
    13481219544761589253,
    14606789564860859588,
    15121068037230253187,
    15142514309343002422,
    15175187352682516539,
    15247016410827505256,
    15381591922765245005,
    15496541866747455224,
    15516999470143134014,
    15584373692268770493,
    15816932127641127812,
    16133730422764900471,
    16207052597670513930,
    16261581317828248693,
    16317939884990355111,
    16650537410730303253,
    17168887746413078989,
    17377110155852733375,
    17389450053896350323,
    17514158411559152738,
    17580604489947609609,
    17834271064829410200,
    17928597985082702189,
    17980184447518608252,
    18136322344440449722,
    18245583872910433339,
    18446744073709551615,
]


class TestStrictUnsignedLongLong(unittest.TestCase):
    def test_pack(self):
        for i in DATA:
            self.assertEqual(pyparcel.pack(UnsignedLongLong(i)), struct.pack("=Q", i))

    def test_pack_unpack(self):
        for i in DATA:
            self.assertEqual(
                UnsignedLongLong(i),
                pyparcel.unpack(pyparcel.pack(UnsignedLongLong(i)), UnsignedLongLong()),
            )


if __name__ == "__main__":
    unittest.main()