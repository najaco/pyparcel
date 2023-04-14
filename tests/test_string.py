import struct
import unittest
from typing import List

import pyparcel
from tests.config import ENCODING

DATA: List[str] = [
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

ENCODINGS: List[str] = ["utf-8", "utf-16", "utf-32", "ascii"]
FAKE_ENCODINGS: List[str] = [
    "",
    " ",
    "fake_encoding1",
    "utf-9",
    "utf-15",
    "utf-17",
    "Hello World",
    "ASCI",
    "a" * 100,
]


class TestString(unittest.TestCase):
    def test_load(self):
        for i in DATA:
            self.assertEqual(
                pyparcel.load(i),
                struct.pack("=i{}s".format(len(i)), len(i), i.encode(ENCODING)),
            )

    def test_load_unload(self):
        for i in DATA:
            self.assertEqual(i, pyparcel.unload(pyparcel.load(i), str()))

    def test_load_with_encodings(self):
        for s in DATA:
            for e in ENCODINGS:
                self.assertEqual(
                    pyparcel.load(s, encoding=e),
                    struct.pack(
                        "=i{}s".format(len(s.encode(e))), len(s.encode(e)), s.encode(e)
                    ),
                    f"Failed with obj = {s} and encoding = {e}",
                )

    def test_load_unload_with_encodings(self):
        for s in DATA:
            for e in ENCODINGS:
                self.assertEqual(
                    s, pyparcel.unload(pyparcel.load(s, encoding=e), str(), encoding=e)
                )

    def test_load_invalid_encoding_throws_exception(self):
        for e in FAKE_ENCODINGS:
            self.assertRaises(Exception, pyparcel.load, DATA[6], encoding=e)

    def test_unload_invalid_encoding_throws_exception(self):
        for e in FAKE_ENCODINGS:
            self.assertRaises(
                Exception, pyparcel.unload, pyparcel.load(DATA[6]), str(), encoding=e
            )


if __name__ == "__main__":
    unittest.main()
