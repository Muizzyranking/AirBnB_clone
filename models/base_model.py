#!/usr/bin/python3
import uuid
from datetime import datetime

from models.engine import storage  # noqa: F401

"""BaseModel class"""


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """init method"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    value = datetime.strptime(value, time_format)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Changes the updated_at attribute to the current datetime
        and saves the instance"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def __str__(self):
        """str method"""
        return_str = "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
        return return_str
