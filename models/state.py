#!/usr/bin/python3
"""This module defines a class 'State' that inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """The state class

        attributes:
            name (str)
    """
    name = ""
