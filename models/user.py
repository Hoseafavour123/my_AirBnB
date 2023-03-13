#!/usr/bin/python3
"""This modules defines a class 'User' that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """A User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
