#!/usr/bin/python3
"""
Unit tests for the BaseModel class and FileStorage class.
"""

import unittest
import os
import json
from datetime import datetime # Corrected import for datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_init_from_dict(self):
        """
        Tests that a BaseModel instance can be created
        from a dictionary.
        """
        model_dict = {
            "id": "12345678-1234-5678-1234-567812345678",
            "created_at": "2023-04-01T12:34:56.789123",
            "updated_at": "2023-04-01T12:34:56.789123",
            "__class__": "BaseModel"
        }
        
        model = BaseModel(**model_dict)
        
        self.assertEqual(model.id, model_dict['id'])
        self.assertEqual(model.created_at, datetime.strptime(model_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f")) # Corrected usage
        self.assertEqual(model.updated_at, datetime.strptime(model_dict["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")) # Corrected usage

    def test_init(self):
        """
        Test that the BaseModel instance is initialized correctly.
        """
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """
        Test the string representation of the BaseModel instance.
        """
        model = BaseModel()
        self.assertIn("BaseModel", str(model))
        self.assertIn(model.id, str(model))

    def test_save(self):
        """
        Test that the save method updates the updated_at attribute.
        """
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method returns a dictionary representation of the instance.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())

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
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage.__file_path)

if __name__ == "__main__":
    unittest.main()
