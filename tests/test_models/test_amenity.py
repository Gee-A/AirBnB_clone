#!/usr/bin/python3
""" unittest """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import os


class TestAmenity(unittest.TestCase):
    """ test """

    @classmethod
    def setUpClass(cls):
        """ create instance """
        cls.ins = Amenity()

    @classmethod
    def teardown(cls):
        """ Delete instance """
        del cls.ins
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_subclass(self):
        """test if class is subclass
            test model doc
            test attributes
            test type
            test if model instance"""
        self.assertEqual(issubclass(Amenity, BaseModel), True)
        self.assertNotEqual(len(Amenity.__doc__), 0)
        self.assertEqual(hasattr(self.ins, "name"), True)
        self.assertEqual(type(self.ins.name), str)
        self.assertTrue(isinstance(self.ins, Amenity))


if __name__ == '__main__':
    unittest.mai()
