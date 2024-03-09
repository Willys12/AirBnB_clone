#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""

import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

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

if __name__ == "__main__":
    unittest.main()
