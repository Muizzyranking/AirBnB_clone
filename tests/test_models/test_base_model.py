#!/usr/bin/python3
"""Test For the BaseModel"""

from models.base_model import BaseModel
import os
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test for the BaseModel class"""

    def setUp(self):
        """Sets up the testing environment"""
        self.base1 = BaseModel()
        self.base2 = BaseModel()

    def tearDown(self):
        """Tears down the testing environment"""
        del self.base1
        del self.base2
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Test for the instantiation of the BaseModel class"""
        self.assertIsInstance(self.base1, BaseModel)
        self.assertIsInstance(self.base2, BaseModel)

    def test_id(self):
        """Test for the id attribute"""
        self.assertIsInstance(self.base1.id, str)
        self.assertIsInstance(self.base2.id, str)
        self.assertNotEqual(self.base1.id, self.base2.id)

    def test_created_at(self):
        """Test for the created_at attribute"""
        self.assertIsInstance(self.base1.created_at, datetime)
        self.assertIsInstance(self.base2.created_at, datetime)

    def test_updated_at(self):
        """Test for the updated_at attribute"""
        self.assertIsInstance(self.base1.updated_at, datetime)
        self.assertIsInstance(self.base2.updated_at, datetime)

    def test_save(self):
        """Test for the save method"""
        old_time1 = self.base1.updated_at
        old_time2 = self.base2.updated_at
        self.base1.save()
        self.base2.save()
        new_time1 = self.base1.updated_at
        new_time2 = self.base2.updated_at
        self.assertNotEqual(old_time1, new_time1)
        self.assertNotEqual(old_time2, new_time2)

    def test_to_dict(self):
        """Test for the to_dict method"""
        base1_dict = self.base1.to_dict()
        base2_dict = self.base2.to_dict()
        self.assertIsInstance(base1_dict, dict)
        self.assertIsInstance(base2_dict, dict)
        self.assertIsInstance(base1_dict["created_at"], str)
        self.assertIsInstance(base2_dict["created_at"], str)
        self.assertIsInstance(base1_dict["updated_at"], str)
        self.assertIsInstance(base2_dict["updated_at"], str)
        self.assertEqual(base1_dict["__class__"], "BaseModel")
        self.assertEqual(base2_dict["__class__"], "BaseModel")

    def test_str(self):
        """Test for the __str__ method"""
        base1_str = self.base1.__str__()
        base2_str = self.base2.__str__()
        self.assertIsInstance(base1_str, str)
        self.assertIsInstance(base2_str, str)
        self.assertEqual(
            base1_str, "[BaseModel] ({}) {}".format(
                self.base1.id, self.base1.__dict__)
        )
        self.assertEqual(
            base2_str, "[BaseModel] ({}) {}".format(
                self.base2.id, self.base2.__dict__)
        )
