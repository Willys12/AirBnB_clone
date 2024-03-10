#!/usr/bin/python3
"""
Unit tests for the FileStorage class.
"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.storage = FileStorage()
        self.storage.all().clear()

    def test_new_and_all(self):
        """
        Test adding a new object and retrieving all objects.
        """
        model = BaseModel()
        self.storage.new(model)
        self.assertIn(f"{model.__class__.__name__}.{model.id}", self.storage.all())

    def test_save_and_reload(self):
        """
        Test saving objects to a file and reloading them.
        """
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.all().clear()
        self.storage.reload()
        self.assertIn(f"{model.__class__.__name__}.{model.id}", self.storage.all())

    def tearDown(self):
        """
        Clean up after each test.
        """
        if os.path.exists(self.storage.__file_path):
            os.remove(self.storage.__file_path)

if __name__ == "__main__":
    unittest.main()
