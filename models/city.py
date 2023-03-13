#!/usr/bin/python3
"""This module defines a class 'City' that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """The City class

        attributes:
            state_id (str).
            name (str).
    """
    state_id = ""
    name = ""
