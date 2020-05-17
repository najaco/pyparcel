import unittest
from typing import Dict
import PyParcel

class MyTestCase(unittest.TestCase):
    class ExampleClassA:
        def __init__(self, a: int, b: float, c: str):
            self.a = a
            self.b = b
            self.c = c

        def to_dict(self) -> Dict:
            return {
                "a": self.a,
                "b": self.b,
                "c": self.c
            }

    def test_pack(self):
        assert 1 == 1



if __name__ == '__main__':
    unittest.main()
