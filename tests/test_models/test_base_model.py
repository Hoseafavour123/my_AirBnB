#!/usr/bin/python3
"""This module contains the tests for BaseModel class"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestInstantiationsAndMagicMethods(unittest.TestCase):
	""" Tests the instantiation parameters for BaseModel. """

	def test_use_of_args(self):
		"""Test if *args is used instead of **kwargs"""
		with self.assertRaises(TypeError):
			my_model = BaseModel('id', 'created_at', 'updated_at')

	def test_empty_arguments(self):
		"""Test for empty arguments in instantiation"""
		my_model = BaseModel()
		self.assertTrue(type(my_model.created_at), datetime)
		self.assertTrue(hasattr(my_model, 'id'))
		self.assertTrue(hasattr(my_model, 'updated_at'))

	def test_new_instance_creation(self):
		"""Test if a new instance is created successfully."""
		my_model = BaseModel()
		my_model.name = "First model"
		my_model.my_number = 89
		my_model_json = my_model.to_dict()
		self.assertTrue(type(my_model_json['created_at']), str)

		new_model = BaseModel(**my_model_json)
		self.assertTrue(type(new_model.created_at), datetime)
		self.assertFalse(my_model is new_model)

	def test_str_method(self):
		"""Test string method for instance."""
		test_me = BaseModel()
		class_name = test_me.__class__.__name__
		obj_id = test_me.id
		obj_dict = test_me.__dict__
		obj_str ="[{}] ({}) {}".format(class_name, obj_id, obj_dict)
		self.assertEqual(str(test_me), obj_str)

class TestBaseMethodS(unittest.TestCase):
	"""Test methods"""

	def test_save(self):
		""" Test the save() method. Updates the public instance attribute updated_at
			to current datetime"""
		obj_inst = BaseModel()
		init_id = obj_inst.updated_at
		obj_inst.save()
		updt_id = obj_inst.updated_at
		self.assertNotEqual(init_id, updt_id)

	def test_to_dict(self):
		"""Test the to_dict() method."""
		obj_inst = BaseModel()
		obj_class = obj_inst.__class__.__name__
		obj_id = obj_inst.id
		updated = obj_inst.updated_at.isoformat()
		created = obj_inst.created_at.isoformat()

		my_dict = {
			'id': obj_id,
			'updated_at': updated,
			'created_at': created,
			'__class__': obj_class
		}
		
		self.assertEqual(obj_inst.to_dict(), my_dict)
