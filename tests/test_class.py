import struct
import unittest
from typing import Dict, List
from tests.config import FLOATING_POINT_ACCURACY, ENCODING


import pyparcel


class ExampleClassA:
    def __init__(self, a: int = 0, b: float = 0.0, c: str = ""):
        self.a: int = a
        self.b: float = b
        self.c: str = c

    def to_dict(self) -> Dict:
        return {"a": self.a, "b": self.b, "c": self.c}

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (
                self.a == other.a
                and round(self.b, FLOATING_POINT_ACCURACY)
                == round(other.b, FLOATING_POINT_ACCURACY)
                and self.c == self.c
            )
        return False


DATA: List[ExampleClassA] = [
    ExampleClassA(),
    ExampleClassA(1, 4.35, "Hello"),
    ExampleClassA(57, 4352.2324, "World"),
    ExampleClassA(1 << 31 - 1, 3648.3, "a" * 2 ** 10),
    ExampleClassA(-1 << 31, -324.43, "z" * 2 ** 10),
]


class MyTestCase(unittest.TestCase):
    def test_pack(self):
        for o in DATA:
            self.assertEqual(
                pyparcel.pack(o),
                struct.pack(
                    "ifq{}s".format(len(o.c)), o.a, o.b, len(o.c), o.c.encode(ENCODING)
                ),
            )

    def test_pack_unpack(self):
        for o in DATA:
            self.assertEqual(o, pyparcel.unpack(pyparcel.pack(o), ExampleClassA()))


if __name__ == "__main__":
    unittest.main()
