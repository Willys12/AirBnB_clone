#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import storage


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        storage.all().clear()

    def test_save(self):
        """
        Test saving a BaseModel instance.
        """
        model = BaseModel()
        model.save()
        self.assertIn(f"{model.__class__.__name__}.{model.id}", storage.all())

    def tearDown(self):
        """
        Clean up after each test.
        """
        storage.all().clear()


if __name__ == "__main__":
    unittest.main()
