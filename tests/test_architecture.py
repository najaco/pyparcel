import struct
import unittest
from typing import Dict, List, Any

from pyparcel import Architecture, StrictType
from tests.config import FLOATING_POINT_ACCURACY, ENCODING

import pyparcel


class ExampleClassA:
    def __init__(self, a: int = 0, b: float = 0.0):
        self.a: int = a
        self.b: float = b

    def to_dict(self) -> Dict[str, Any]:
        return {"a": self.a, "b": self.b}

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (
                    self.a == other.a
                    and round(self.b, FLOATING_POINT_ACCURACY)
                    == round(other.b, FLOATING_POINT_ACCURACY)
            )
        return False


class ExampleClassB:
    def __init__(self, a: int = 0, b: float = 0.0, c: str = ""):
        self.a: int = a
        self.b: float = b
        self.c: str = c

    def to_dict(self) -> Dict[str, Any]:
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


DATA: List[ExampleClassB] = [
    ExampleClassB(),
    ExampleClassB(1, 4.35, "Hello"),
    ExampleClassB(57, 4352.2324, "World"),
    ExampleClassB(1 << 31 - 1, 3648.3, "a" * 2 ** 10),
    ExampleClassB(-1 << 31, -324.43, "z" * 2 ** 10),
]


class MyTestCase(unittest.TestCase):
    def test_pack_x86(self):
        for o in DATA:
            self.assertEqual(
                pyparcel.pack(o),
                struct.pack(
                    "ifi{}s".format(len(o.c)), o.a, o.b, len(o.c), o.c.encode(ENCODING)
                ),
            )

    def test_pack_unpack_x86(self):
        for o in DATA:
            self.assertEqual(o, pyparcel.unpack(pyparcel.pack(o), ExampleClassB()))

    def test_pack_different_arch_simple(self):
        custom_architecture = Architecture(sint=StrictType.LONG_LONG,
                                           sfloat=StrictType.DOUBLE, str_length=StrictType.UNSIGNED_LONG)
        custom_pack = pyparcel.generate_pack_with_architecture(custom_architecture)
        o = ExampleClassA(8, 5.7)
        self.assertEqual(custom_pack(o), struct.pack("qd", o.a, o.b))

    def test_pack_unpack_different_arch_simple(self):
        custom_architecture = Architecture(str_length=StrictType.UNSIGNED_LONG, sint=StrictType.LONG_LONG,
                                           sfloat=StrictType.DOUBLE)
        custom_pack = pyparcel.generate_pack_with_architecture(custom_architecture)
        custom_unpack = pyparcel.generate_unpack_with_architecture(custom_architecture)
        o = ExampleClassA(8, 5.7)
        self.assertEqual(o, custom_unpack(custom_pack(o), o.__class__()))

    def test_pack_different_arch_str(self):
        custom_architecture = Architecture(str_length=StrictType.UNSIGNED_LONG)
        custom_pack = pyparcel.generate_pack_with_architecture(custom_architecture)
        test_string = "Hello World!"
        self.assertEqual(custom_pack(test_string), struct.pack("L{}s".format(len(test_string)), len(test_string), test_string.encode(ENCODING)))

    def test_pack_unpack_different_arch_str(self):
        custom_architecture = Architecture(str_length=StrictType.UNSIGNED_LONG)
        test_string = "Hello World!"
        custom_pack = pyparcel.generate_pack_with_architecture(custom_architecture)
        custom_unpack = pyparcel.generate_unpack_with_architecture(custom_architecture)
        self.assertEqual(test_string, custom_unpack(custom_pack(test_string), test_string.__class__()))

    def test_pack_different_arch_adv(self):
        custom_architecture = Architecture(sint=StrictType.LONG_LONG,
                                           sfloat=StrictType.DOUBLE, str_length=StrictType.UNSIGNED_LONG)
        custom_pack = pyparcel.generate_pack_with_architecture(custom_architecture)
        for o in DATA:
            self.assertEqual(
                custom_pack(o),
                struct.pack(
                    "qdL{}s".format(len(o.c)), o.a, o.b, len(o.c), o.c.encode(ENCODING)
                ),
            )

    def test_pack_unpack_different_arch_adv(self):
        custom_architecture = Architecture(str_length=StrictType.UNSIGNED_LONG, sint=StrictType.LONG_LONG,
                                           sfloat=StrictType.DOUBLE)
        custom_pack = pyparcel.generate_pack_with_architecture(custom_architecture)
        custom_unpack = pyparcel.generate_unpack_with_architecture(custom_architecture)

        for o in DATA:
            self.assertEqual(o, custom_unpack(custom_pack(o), o.__class__()))


if __name__ == "__main__":
    unittest.main()
