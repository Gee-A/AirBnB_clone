#!/usr/bin/python3
"""Unittest module: Test FileStorage Class."""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """Test Cases for FileStorage Class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def test_5_instantiation(self):
        """Tests instantiation of storage class."""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_init_no_args(self):
        """Tests __init__ with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), msg)

    def test_init_many_args(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            fs = FileStorage(0, 1, 2, 4, 5, 6, 7, 8, 9)
        msg = "FileStorage() takes no arguments"
        self.assertEqual(str(e.exception), msg)

    def test_5_attributes(self):
        """Tests class attributes."""
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def test_5_new_no_args(self):
        """Tests new() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            storage.new()
        msg = "FileStorage.new() missing 1 required positional argument: 'obj'"
        self.assertEqual(str(e.exception), msg)

    def test_5_new_excess_args(self):
        """Tests new() with more than the required arguments."""
        self.resetStorage()
        b = BaseModel()
        with self.assertRaises(TypeError) as e:
            storage.new(b, 98)
        msg = "FileStorage.new() takes 2 positional arguments but 3 were given"
        self.assertEqual(str(e.exception), msg)

    def test_5_save_no_args(self):
        """Tests save() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save()
        msg = "FileStorage.save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_save_excess_args(self):
        """Tests save() with more than the required arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 98)
        msg = "FileStorage.save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_5_reload_no_args(self):
        """Tests reload() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.reload()
        msg = "FileStorage.reload() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_reload_excess_args(self):
        """Tests reload() with more than the reqiured arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.reload(self, 98)
        msg = "FileStorage.reload() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)
