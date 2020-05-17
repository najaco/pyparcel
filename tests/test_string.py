import struct
import unittest
from typing import List

import pyparcel
from tests.config import ENCODING


class MyTestCase(unittest.TestCase):
    def test_pack(self):
        data: List[int] = [
            "",
            "Hello",
            "World",
            "Hello World",
            " ",
            "Some sentence here.",
            "abcdefghijklmnopqrstuvwxyz",
            "123456789",
            "`-=[]\\;',./~_+{}|:\"<>?",
            "a" * 2 ** 20,
            " " * 2 ** 20,
        ]
        for i in data:
            assert pyparcel.pack(i) == struct.pack(
                "q{}s".format(len(i)), len(i), i.encode(ENCODING)
            )

    def test_pack_unpack(self):

        data: List[int] = [
            "",
            "Hello",
            "World",
            "This is a very very very long string",
            "a" * 2 ** 20,
        ]

        for i in data:
            assert i == pyparcel.unpack(pyparcel.pack(i), str())


if __name__ == "__main__":
    unittest.main()
