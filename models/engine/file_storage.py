#!/usr/bin/env python3
"""
FileStorage class for serializing and deserializing instances
to/from a JSON file.
"""
import json
import os


class FileStorage:
    """
    Handles the serialization and deserialization of instances to and
    from a JSON file.Ensures persistence across program launches.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all stored objects."""
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj (BaseModel): The object to be stored.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes all objects to the JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump({k: obj.to_dict() for k,
                       obj in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to objects.
        Only if the JSON file exists; otherwise, does nothing.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj_dict in data.items():
                    class_name = obj_dict['__class__']
                    if class_name in globals():
                        cls = globals()[class_name]
                        obj = cls(**obj_dict)
                        self.new(obj)
