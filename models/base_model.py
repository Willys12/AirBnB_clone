#!/usr/bin/python3
"""
BaseModel class that defines common attributes and methods for other classes.
"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    BaseModel class that provides common attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BaseModel class.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        # Handle additional attributes passed as kwargs
        for k, v in kwargs.items():
            if k == "__class__":
                continue
            if k in ["created_at", "updated_at"]:
                # Convert string to datetime object if necessary
                if isinstance(v, str):
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__[k] = v
        # Add the new instance to storage if it's not from a dictionary representation
        if not kwargs:
            storage.new(self)

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the updated_at attribute to the current datetime and save the instance.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel instance.
        """
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = self.__class__.__name__
        model_dict["created_at"] = self.created_at.isoformat()
        model_dict["updated_at"] = self.updated_at.isoformat()
        return model_dict
