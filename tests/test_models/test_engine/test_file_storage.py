#!/usr/bin/python3
"""
Unittests for FileStorage.
"""
import os
import unittest
import pycodestyle
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class FileStorageTests(unittest.TestCase):
    """
    FileStorage tests.
    """
    bm = BaseModel()

    def testInstance(self):
        """
        Check instance correct.
        """
        self.assertIsInstance(storage, FileStorage)

    def testHasAttributes(self):
        """
        Check if attributes exist.
        """
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def testSaveBaseModel(self):
        """
        Check save BaseModel
        """
        self.bm.name = "new BaseModel"
        self.bm.save()
        bm_dict_1 = self.bm.to_dict()
        st_dict = storage.all()
        key = bm_dict_1['__class__'] + "." + bm_dict_1['id']
        self.assertEqual(key in st_dict, True)
        self.assertEqual(bm_dict_1['name'], "new BaseModel")

        self.bm.name = "update BaseModel"
        self.bm.save()
        bm_dict_2 = self.bm.to_dict()
        st_dict = storage.all()
        key = bm_dict_2['__class__'] + "." + bm_dict_2['id']
        self.assertEqual(key in st_dict, True)
        self.assertEqual(bm_dict_2['name'], "update BaseModel")

        self.assertEqual(bm_dict_1["id"], bm_dict_2["id"])
        self.assertEqual(bm_dict_1["created_at"], bm_dict_2["created_at"])
        self.assertNotEqual(bm_dict_1["updated_at"], bm_dict_2["updated_at"])

    def testMethodSave(self):
        """
        Check method save and file JSOM
        """
        self.bm.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def testMethodReload(self):
        """
        Check method reload and file JSOM
        """
        self.bm.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        objects_dict = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(objects_dict, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(objects_dict[key].to_dict(), value.to_dict())


class CodeStyleTests(unittest.TestCase):
    """
    Code style test.
    """

    def testPycodestyle(self):
        """
        Tests cases for pycodestyle.
        """
        code_style = pycodestyle.StyleGuide(quiet=True)
        result = code_style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(result.total_errors, 0,
                         "FileStorage pycodestyle error")


class DocumentationTests(unittest.TestCase):
    """
    Documentation test.
    """

    def testDocString(self):
        """
        Tests cases for docstring.
        """
        self.assertIsNotNone(models.FileStorage.__doc__,
                             "FileStorage not docstring")


if __name__ == "__main__":
    unittest.main()
