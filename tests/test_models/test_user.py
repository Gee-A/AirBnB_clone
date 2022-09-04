#!/usr/bin/python3
""" unittest """
import unittest
from models.user import User
from models.base_model import BaseModel
import os


class TestUser(unittest.TestCase):
    """ test """

    @classmethod
    def setUpClass(cls):
        """ create instance """
        cls.ins = User()

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
        self.assertEqual(issubclass(User, BaseModel), True)

    def test_doc(self):
        """ test model doc """
        self.assertNotEqual(len(User.__doc__), 0)

    def test_attr(self):
        """ test model attributes """
        self.assertEqual(hasattr(self.ins, "email"), True)
        self.assertEqual(hasattr(self.ins, "password"), True)
        self.assertEqual(hasattr(self.ins, "first_name"), True)
        self.assertEqual(hasattr(self.ins, "last_name"), True)

    def test_type(self):
        """ test type of object """
        self.assertEqual(type(self.ins.email), str)
        self.assertEqual(type(self.ins.password), str)
        self.assertEqual(type(self.ins.first_name), str)
        self.assertEqual(type(self.ins.last_name), str)

    def test_isinstance(self):
        """ test isinstance """
        self.assertTrue(isinstance(self.ins, User))


if __name__ == '__main__':
    unittest.main()
