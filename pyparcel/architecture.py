from typing import Any, Dict
from .strict_type import StrictType


class Architecture:
    def __init__(
        self,
        sint: StrictType = StrictType.INT,
        sbool: StrictType = StrictType.BOOL,
        sfloat: StrictType = StrictType.FLOAT,
        sstr: StrictType = StrictType.CHAR_ARR,
        sbytes: StrictType = StrictType.CHAR_ARR,
        str_length: StrictType = StrictType.INT,
        encoding: str = "utf-8",
    ):
        self._data: Dict[Any, StrictType] = {
            int: sint,
            bool: sbool,
            float: sfloat,
            str: sstr,
            bytes: sbytes,
            "str_length": str_length,
        }
        self.encoding = encoding

    def __getitem__(self, key: Any) -> StrictType:
        if key not in self._data:
            raise IndexError
        return self._data[key]

    def size_of(self, key: Any) -> int:
        if key not in self._data:
            raise IndexError
        return self._data[key].value.size

    def format_of(self, key: Any) -> str:
        if key not in self._data:
            raise IndexError
        return self._data[key].value.format
