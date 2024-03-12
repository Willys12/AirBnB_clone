#!/usr/bin/python3
import unittest
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = HBNBCommand()

    def test_create(self):
        # Simulate creating an instance
        # This test assumes do_create prints the ID of the created instance
        # You might need to adjust this based on your actual implementation
        self.assertIsNotNone(self.cmd.do_create("BaseModel"))

    def test_show(self):
        # Simulate showing an instance
        # This test assumes do_show prints the instance if found
        # You might need to adjust this based on your actual implementation
        self.assertIsNotNone(self.cmd.do_show("BaseModel 1234-1234-1234"))

    def test_destroy(self):
        # Simulate destroying an instance
        # This test assumes do_destroy prints a success message if the instance is found
        # You might need to adjust this based on your actual implementation
        self.assertIsNotNone(self.cmd.do_destroy("BaseModel 1234-1234-1234"))

    def test_all(self):
        # Simulate listing all instances
        # This test assumes do_all prints all instances if no class is specified
        # You might need to adjust this based on your actual implementation
        self.assertIsNotNone(self.cmd.do_all(""))

    def test_update(self):
        # Simulate updating an instance
        # This test assumes do_update prints a success message if the instance is found
        # You might need to adjust this based on your actual implementation
        self.assertIsNotNone(self.cmd.do_update("BaseModel 1234-1234-1234 name 'New Name'"))

if __name__ == '__main__':
    unittest.main()
