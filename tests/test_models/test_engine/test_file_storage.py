#!/usr/bin/python3
""" This module contain the tests for file_storage.py located at
models/engine/file_storage.py
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import uuid
from os import path


class FileStorageTest(unittest.TestCase):
    """Test file storage"""
    def setUp(self):
        """set up"""
        self.storage = FileStorage()

    def test_private_attributes(self):
        """test private attributes."""
        with self.assertRaises(AttributeError):
            err_obj = self.storage.__objects
        with self.assertRaises(AttributeError):
            err_path = self.storage.__file_path

    def test_all(self):
        """test the all() method when an object is added to storage"""
        my_model = BaseModel()
        self.assertTrue(type(self.storage.all()), dict)

    def test_save(self):
        """test the save() method"""
        self.storage.save()
        self.assertTrue(path.isfile("file.json"))

    def test_reload(self):
        """test reload"""
        self.assertTrue(self.storage.reload, None)
