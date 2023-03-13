#!/usr/bin/python3
"""This module defines a class 'Amenity' that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The Amenity class

        attributes:
            name (str)
    """
    name = ""
