import unittest
from typing import List
import re
import pyparcel

NECESSARY_VARS: List[str] = ['__title__', '__description__', '__url__', '__version__', '__author__',
                             '__author_email__', '__license__']


class TestProject(unittest.TestCase):

    def test_fields_exist(self):
        for v in NECESSARY_VARS:
            try:
                eval('pyparcel.' + v)
            except AttributeError:
                self.fail(f"pyparcel.{v} failed")

    def test_fields_have_text(self):
        for v in NECESSARY_VARS:
            try:
                s = eval('pyparcel.' + v)
                self.assertTrue(len(s) != 0, f"pyparcel.{v} does not contain any text")
            except AttributeError:
                self.fail(f"pyparcel.{v} failed")


    def test_version_format(self):
        if '__version__' in pyparcel.__dict__:
            self.assertTrue(re.match(r"\d+.\d+.\d+", pyparcel.__version__))
        else:
            self.fail('__version__ not found in pyparcel.__dict__')

    def test_email_format(self):
        if '__author_email__' in pyparcel.__dict__:
            self.assertTrue(re.match(r".+@.*\.(com|org|net)", pyparcel.__author_email__))
        else:
            self.fail('__version__ not found in pyparcel.__dict__')


if __name__ == '__main__':
    unittest.main()
