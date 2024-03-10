#!/usr/bin/python3
import uuid
from datetime import datetime

# from models.engine import storage  # noqa: F401

"""
Module containing the BaseModel class.

The BaseModel class defines the core attributes and methods that is
common to all other models within the application.

This includes:

* A unique id for each instance
* Tracking the time of creation and update of each instance
* Serialization and deserialization of instances to and from JSON format
"""


class BaseModel:
    """
    Defines the base class for all models within the application.

    Attributes:
        id (str): A unique id for each instance
        created_at (datetime): The time of creation of the instance
        updated_at (datetime): The time of update of the instance

    Methods:
        save: Changes the updated_at attribute to the current datetime
        and saves the instance
        to_dict: Returns a dictionary containing all keys/values of __dict__
        __str__: Returns a string representation of the instance
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
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
