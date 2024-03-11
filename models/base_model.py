#!/usr/bin/env python3
import uuid
from datetime import datetime


class BaseModel:
    """Base model class for the common methods"""

    def __init__(self, *args, **kwargs):
        """Initializes Basemodel"""
        if kwargs:
            self.__set_attr(**kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __set_attr(self, **kwargs):
        """Sets attributes from keyworded arguments"""
        if 'id' in kwargs:
            self.id = kwargs['id']
        else:
            self.id = str(uuid.uuid4())
        if 'created_at' in kwargs:
            self.created_at = datetime.strptime(kwargs['created_at'],
                                                "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.created_at = datetime.now()
        if 'updated_at' in kwargs:
            self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                "%Y-%m-%dT%H:%M:%S.%f")

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values"""
        obj_dict = {
            key: value.isoformat() if isinstance(value, datetime) else value
            for key, value in self.__dict__.items()
        }
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """Returns string rep. of object"""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
        