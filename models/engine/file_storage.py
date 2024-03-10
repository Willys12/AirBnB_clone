#!/usr/bin/python3
"""
FileStorage class that serializes instance to a JSON
file and deserialize JSON file to instances
"""

import json
import os


class FileStorage:
    """
    FileStorage class for serializing and deserializing
    instances to/from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary of all objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new object to the storage.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serialize all objects to the JSON file.
        """
        with open(self.__file_path, 'w') as file:
            file.write(json.dumps({k: obj.to_dict() for k,
                                   obj in self.__objects.items()}))

    def reload(self):
        """
        Deserialize the JSON file to objects.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    cls_name, obj_id = key.split('.')
                    cls = globals()[cls_name]
                    obj = cls.form_dict(obj_dict)
                    self.new(obj)
