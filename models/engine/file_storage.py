#!/usr/bin/python3
import json

"""This module defines a class to manage file storage for hbnb clone"""


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = "storage.json"
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(new_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                new_dict = json.load(file)
            for value in new_dict.values():
                class_name = value["__class__"]
                del value["__class__"]
                self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass
