#!/usr/bin/python3
"""
Unittests for Amenity.
"""
import unittest
import pycodestyle
import datetime
import models
from models.base_model import BaseModel
from models.amenity import Amenity


class AmenityTests(unittest.TestCase):
    """
    Amenity tests.
    """
    am = Amenity()

    def testAttributes(self):
        """
        Test cases for the attributes.
        """
        self.am.name = "New Amenity"
        dict_am = self.am.to_dict()

        self.assertEqual(self.am.name, dict_am["name"])
        self.assertEqual("Amenity", dict_am["__class__"])

    def testInheritance(self):
        """
        Test cases verify is subclass of BaseModel
        """
        self.assertIsInstance(self.am, BaseModel)
        self.assertTrue(hasattr(self.am, 'id'))
        self.assertTrue(hasattr(self.am, 'created_at'))
        self.assertTrue(hasattr(self.am, 'updated_at'))

    def testTypeAttributes(self):
        """
        Test case for validate type for attributes.
        """
        self.assertIsInstance(self.am.name, str)
        self.assertIsInstance(self.am.id, str)
        self.assertIsInstance(self.am.created_at, datetime.datetime)
        self.assertIsInstance(self.am.updated_at, datetime.datetime)

    def testDateUpdate(self):
        """
        Test case for validate change update_at.
        """
        self.am.name = "Update 1"
        self.am.save()
        dict_1 = self.am.to_dict()

        self.am.name = "Update 2"
        self.am.save()
        dict_2 = self.am.to_dict()

        self.assertEqual(dict_1["id"], dict_2["id"])
        self.assertEqual(dict_1["created_at"], dict_2["created_at"])
        self.assertNotEqual(dict_1["updated_at"], dict_2["updated_at"])
        self.assertNotEqual(dict_1["name"], dict_2["name"])


class CodeStyleTests(unittest.TestCase):
    """
    Code style test.
    """

    def testPycodestyle(self):
        """
        Tests cases for pycodestyle.
        """
        code_style = pycodestyle.StyleGuide(quiet=True)
        result = code_style.check_files(["models/amenity.py"])
        self.assertEqual(result.total_errors, 0, "Amenity pycodestyle error")


class DocumentationTests(unittest.TestCase):
    """
    Documentation test.
    """

    def testDocString(self):
        """
        Tests cases for docstring.
        """
        self.assertIsNotNone(models.amenity.__doc__,
                             "Amenity not docstring")


if __name__ == "__main__":
    unittest.main()
