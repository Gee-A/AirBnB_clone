#!/usr/bin/python3
""" unittest """
import unittest
from models.review import Review
from models.base_model import BaseModel
import os


class TestReview(unittest.TestCase):
    """ test """

    @classmethod
    def setUpClass(cls):
        """ create instance """
        cls.ins = Review()

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
        self.assertEqual(issubclass(Review, BaseModel), True)

    def test_doc(self):
        """ test model doc """
        self.assertNotEqual(len(Review.__doc__), 0)

    def test_attr(self):
        """ test model attributes """
        self.assertEqual(hasattr(self.ins, "place_id"), True)
        self.assertEqual(hasattr(self.ins, "user_id"), True)
        self.assertEqual(hasattr(self.ins, "text"), True)

    def test_type(self):
        """ test type of object """
        self.assertEqual(type(self.ins.place_id), str)
        self.assertEqual(type(self.ins.user_id), str)
        self.assertEqual(type(self.ins.text), str)

    def test_isinstance(self):
        """ test isinstance """
        self.assertTrue(isinstance(self.ins, Review))


if __name__ == '__main__':
    unittest.main()
