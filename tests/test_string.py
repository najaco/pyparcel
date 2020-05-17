import unittest
from typing import Dict, List
import pyparcel
import struct


class MyTestCase(unittest.TestCase):
    class ExampleClassA:
        def __init__(self, a: int, b: float, c: str):
            self.a = a
            self.b = b
            self.c = c

        def to_dict(self) -> Dict:
            return {"a": self.a, "b": self.b, "c": self.c}

    def test_pack(self):
        data: List[int] = [
            "",
            "Hello",
            "World",
            "This is a very very very long string",
            "a" * 2 ** 20,
        ]
        for i in data:
            assert pyparcel.pack(i) == struct.pack(
                "q{}s".format(len(i)), len(i), i.encode("utf-8")
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
