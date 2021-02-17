#!/usr/bin/python3
"""Defines unnittests for the class BaseModel"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Performs unittests for the base model class"""

    @classmethod
    def setUpClass(cls):
        """Instantiates the BaseModel class for testing
        renames the output file(file.json)
        """
        cls.base_inst = BaseModel()
        try:
            os.rename("file.json", "orignal_f")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Performs cleanup
           Restores the original file.json
        """
       #  del cls.base_inst
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("oginal", "file.json")
        except:
            pass

    def test_pep8(self):
        pep_8 = pep8.StyleGuide(quiet=True)
        result = pep_8.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Pep8 Style error")

    def test_instance(self):
        """verify that an instance of BaseModel exists"""
        self.assertIsInstance(self.base_inst, BaseModel)

    def test_create(self):
        self.base_inst.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_attributes(self):
        """Check for attribute type compliance."""
        self.assertEqual(str, type(self.base_inst.id))
        self.assertEqual(datetime, type(self.base_inst.created_at))
        self.assertEqual(datetime, type(self.base_inst.updated_at))

    def test_docstring(self):
        """Check docstring implementation"""
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)

    def test_methods(self):
        """Test if required methods are implemented."""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "__str__"))

    def test_init(self):
        """Test initialization of the model"""
        self.assertIsInstance(self.base_inst, BaseModel)

    def test_model_uniqueness(self):
        """Test that different BaseModel instances are unique."""
        base_model = BaseModel()
        self.assertNotEqual(self.base_inst.id, base_model.id)

    def test_save(self):
        """ Test save method """
        self.base_inst.save()
        self.assertNotEqual(self.base_inst.created_at, self.base_inst.updated_at)
        self.old = self.base_inst.updated_at
        self.base_inst.save()
        self.new = self.base_inst.updated_at
        self.assertIsNot(self.old, self.new)

    

if __name__ == "__main__":
    unittest.main()
