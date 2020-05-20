from enum import Enum
from collections import namedtuple


TypeData = namedtuple("TypeData", ["format", "size"])


class StrictType(Enum):
    """Represents the strict types that are found in statically typed languages.
    """

    PAD_BYTE = TypeData("x", 1)
    CHAR = TypeData("c", 1)
    SIGNED_CHAR = TypeData("b", 1)
    UNSIGNED_CHAR = TypeData("B", 1)
    BOOL = TypeData("?", 1)
    SHORT = TypeData("h", 2)
    UNSIGNED_SHORT = TypeData("H", 2)
    INT = TypeData("i", 4)
    UNSIGNED_INT = TypeData("I", 4)
    LONG = TypeData("l", 4)
    UNSIGNED_LONG = TypeData("L", 4)
    LONG_LONG = TypeData("q", 8)
    UNSIGNED_LONG_LONG = TypeData("Q", 8)
    FLOAT = TypeData("f", 4)
    DOUBLE = TypeData("d", 8)
    CHAR_ARR = TypeData("{}s", 8)
