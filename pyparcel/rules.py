from .strict_type import StrictType
from typing import Any, Dict


class Rules:
    """Rules that pyparcel follows when packing/unpacking information.
    """
    def __init__(self):
        self._representation: Dict[Any, StrictType] = {
            int: StrictType.INT,
            bool: StrictType.BOOL,
            float: StrictType.FLOAT,
            "str_length": StrictType.INT
        }

    def represent(self, t: Any, strict_type: StrictType):
        self._representation[t] = strict_type
        return self

    def sizeof(self, t: Any):
        return self._representation[t].value.size
