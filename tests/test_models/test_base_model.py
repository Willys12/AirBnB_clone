import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()
        
    def tearDown(self):
        del self.base_model
        
    def test_attributes(self):
        self.asserTrue(hasattr(self.base_model, 'id'))
        self.asserTrue(hasattr(self.base_model, 'created_at'))
        self.asserTrue(hasattr(self.base_model, 'updated_at'))
        
    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)
    
    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)
    
    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.update_at, datetime)
        
    def test_save_update_updated_at(self):
        old_update_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)
        
    def test_to_dict(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__clas__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], self.base_model.id)
        self.assertEqual(obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.base_model.updated_at.isoformat())
        
    def test_str_representation(self):
        str_representation = str(self.base_model)
        self.assertTrue(str_representation.startswitch('[BaseModel]'))
        self.assertIn(self.base_model.id, str_representation)
        self.assertIn(str(self.base_model.__dict__), str_representation)
        
        
if __name__ == '__main__':
    unittest.main()