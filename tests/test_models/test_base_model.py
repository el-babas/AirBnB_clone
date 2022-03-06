#!/usr/bin/python3
"""
Class definition
"""
from models.base_model import BaseModel
import unittest


class TestModules(unittest.TestCase):
    """
    Class definition
    """
    def testEquals(self):
        """
        Method definition
        """
        self.assertEqual(3, 3)

if __name__ == "__main__":
    unittest.main()
