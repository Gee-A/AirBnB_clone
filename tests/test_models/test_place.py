#!/usr/bin/python3
""" unittest """
import unittest
from models.place import Place
from models.base_model import BaseModel
import os


class TestPlace(unittest.TestCase):
    """ test """

    @classmethod
    def setUpClass(cls):
        """ create instance """
        cls.ins = Place()

    @classmethod
    def teardown(cls):
        """ Delete instance """
        del cls.ins
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_subclass(self):
        """test if class is subclass"""
        self.assertEqual(issubclass(Place, BaseModel), True)

    def test_doc(self):
        """ test model doc """
        self.assertNotEqual(len(Place.__doc__), 0)

    def test_attr(self):
        """ test model attributes """
        self.assertEqual(hasattr(self.ins, "city_id"), True)
        self.assertEqual(hasattr(self.ins, "user_id"), True)
        self.assertEqual(hasattr(self.ins, "name"), True)
        self.assertEqual(hasattr(self.ins, "description"), True)
        self.assertEqual(hasattr(self.ins, "number_rooms"), True)
        self.assertEqual(hasattr(self.ins, "number_bathrooms"), True)
        self.assertEqual(hasattr(self.ins, "max_guest"), True)
        self.assertEqual(hasattr(self.ins, "price_by_night"), True)
        self.assertEqual(hasattr(self.ins, "latitude"), True)
        self.assertEqual(hasattr(self.ins, "longitude"), True)
        self.assertEqual(hasattr(self.ins, "amenity_ids"), True)

    def test_type(self):
        """ test type of object """
        self.assertEqual(type(self.ins.city_id), str)
        self.assertEqual(type(self.ins.user_id), str)
        self.assertEqual(type(self.ins.name), str)
        self.assertEqual(type(self.ins.description), str)
        self.assertEqual(type(self.ins.number_rooms), int)
        self.assertEqual(type(self.ins.number_bathrooms), int)
        self.assertEqual(type(self.ins.max_guest), int)
        self.assertEqual(type(self.ins.price_by_night), int)
        self.assertEqual(type(self.ins.latitude), float)
        self.assertEqual(type(self.ins.longitude), float)
        self.assertEqual(type(self.ins.amenity_ids), list)

    def test_isinstance(self):
        """ test isinstance """
        self.assertTrue(isinstance(self.ins, Place))


if __name__ == '__main__':
    unittest.main()
