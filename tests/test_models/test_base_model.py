#!/usr/bin/python3
"""
Unittests for BaseModel.
"""
import unittest
import pycodestyle
import datetime
import models
from models.base_model import BaseModel


class BaseModelTests(unittest.TestCase):
    """
    BaseModel tests.
    """
    bm = BaseModel()

    def testAttributes(self):
        """
        Test cases for the attributes.
        """
        self.bm.name = "New Base Model"
        self.bm.my_number = 89
        self.bm.reason = "Test case"
        self.bm.save()
        dict_bm = self.bm.to_dict()

        self.assertEqual(self.bm.id, dict_bm["id"])
        self.assertEqual(self.bm.reason, dict_bm["reason"])
        self.assertEqual(self.bm.my_number, dict_bm["my_number"])
        self.assertEqual(self.bm.reason, dict_bm["reason"])
        self.assertEqual("BaseModel", dict_bm["__class__"])

    def testTypeAttributes(self):
        """
        Test case for validate type for attributes.
        """
        self.assertIsInstance(self.bm.id, str)
        self.assertIsInstance(self.bm.created_at, datetime.datetime)
        self.assertIsInstance(self.bm.updated_at, datetime.datetime)

    def testDateUpdate(self):
        """
        Test case for validate change update_at.
        """
        self.bm.changes = "Update 1"
        self.bm.save()
        dict_1 = self.bm.to_dict()

        self.bm.changes = "Update 2"
        self.bm.save()
        dict_2 = self.bm.to_dict()

        self.assertEqual(dict_1["id"], dict_2["id"])
        self.assertEqual(dict_1["created_at"], dict_2["created_at"])
        self.assertNotEqual(dict_1["updated_at"], dict_2["updated_at"])


class CodeStyleTests(unittest.TestCase):
    """
    Code style test.
    """

    def testPycodestyle(self):
        """
        Tests cases for pycodestyle.
        """
        code_style = pycodestyle.StyleGuide(quiet=True)
        result = code_style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0, "BaseModel pycodestyle error")


class DocumentationTests(unittest.TestCase):
    """
    Documentation test.
    """

    def testDocString(self):
        """
        Tests cases for docstring.
        """
        self.assertIsNotNone(models.base_model.__doc__,
                             "BaseModel not docstring")


if __name__ == "__main__":
    unittest.main()
