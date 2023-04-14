import unittest
import pyparcel


class TestInvalidData(unittest.TestCase):
    def test_data_too_small(self):
        data: bytes = pyparcel.load(1, 2.3)
        self.assertRaises(
            Exception, pyparcel.unload, data[len(data) // 2 :], int(), float()
        )

    def test_data_too_big(self):
        data: bytes = pyparcel.load(1, 2.3)
        print(data)
        self.assertRaises(
            Exception, pyparcel.unload, data + "a".encode("utf-8"), int(), float()
        )


if __name__ == "__main__":
    unittest.main()
