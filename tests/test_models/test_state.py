#!/usr/bin/python3
""" unittest """
import unittest
from models.state import State
from models.base_model import BaseModel
import os


class TestCity(unittest.TestCase):
    """ test """

    @classmethod
    def setUpClass(cls):
        """ create instance """
        cls.ins = State()

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
        self.assertEqual(issubclass(State, BaseModel), True)

    def test_doc(self):
        """ test model doc """
        self.assertNotEqual(len(State.__doc__), 0)

    def test_attr(self):
        """ test model attributes """
        self.assertEqual(hasattr(self.ins, "name"), True)
        self.assertEqual(hasattr(self.ins, "state_id"), True)

    def test_type(self):
        """ test type of object """
        self.assertEqual(type(self.ins.name), str)

    def test_isinstance(self):
        """ test isinstance """
        self.assertTrue(isinstance(self.ins, State))


if __name__ == '__main__':
    unittest.main()
