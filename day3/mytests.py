import unittest
from extra import *

class MyFirstTests(unittest.TestCase):
    def test_custom_missing_number(self):
        self.assertEqual(custom_missing_number([1,2,3,5,6,7,9]), [4,8])