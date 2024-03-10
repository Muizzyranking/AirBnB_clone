#!/usr/bin/python3
"""
Defines the test for the file_storage module
"""

import unittest
from models.base_model import BaseModel
import os
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    Test the file storage
    """

    def setUp(self):
        """
        Set up the test
        """
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        """
        Tear down the test
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """
        Test the all method
        """
        storage.reload()
        all_objs = storage.all()
        self.assertIn("BaseModel.{}".format(self.model1.id), all_objs)
        self.assertIn("BaseModel.{}".format(self.model2.id), all_objs)

    def test_new(self):
        """
        Test the new method
        """
        storage.reload()
        model3 = BaseModel()
        all_objs = storage.all()
        self.assertIn("BaseModel.{}".format(model3.id), all_objs)

    def test_save(self):
        """
        Test the save method
        """
        storage.reload()
        model3 = BaseModel()
        storage.save()
        with open("file.json", "r") as file:
            self.assertIn("BaseModel.{}".format(model3.id), file.read())

    def test_reload(self):
        """
        Test the reload method
        """
        storage.reload()
        storage.save()
        all_objs = storage.all()
        self.assertIn("BaseModel.{}".format(self.model1.id), all_objs)
        self.assertIn("BaseModel.{}".format(self.model2.id), all_objs)
