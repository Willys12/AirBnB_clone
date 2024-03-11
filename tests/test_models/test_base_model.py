#!/usr/bin/python3
"""
Tests for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """
    Tests for the BaseModel class.
    """

    def setUp(self):
        """
        Setup for the tests.
        """
        self.storage = FileStorage()
        self.storage.reload()

    def test_create_base_model(self):
        """
        Tests creating a BaseModel instance.
        """
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_base_model_attributes(self):
        """
        Tests setting and getting attributes of a BaseModel instance.
        """
        model = BaseModel()
        model.name = "Test Model"
        self.assertEqual(model.name, "Test Model")

    def test_base_model_save(self):
        """
        Tests the save method of a BaseModel instance.
        """
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)

    def test_base_model_persistence(self):
        """
        Tests that a BaseModel instance is saved and can be reloaded.
        """
        model = BaseModel()
        model.save()
        self.storage.reload()
        reloaded_model = (
            self.storage.all().get(
                f"{model.__class__.__name__}.{model.id}"
                )
            )
        self.assertIsNotNone(reloaded_model)
        self.assertEqual(model.id, reloaded_model.id)
        self.assertEqual(model.created_at, reloaded_model.created_at)
        self.assertEqual(model.updated_at, reloaded_model.updated_at)


if __name__ == '__main__':
    unittest.main()
