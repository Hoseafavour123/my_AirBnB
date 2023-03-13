#!/usr/bin/python3
"""This module defines a class 'Reviews' that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Reviews"""
    place_id = ""
    user_id = ""
    text = ""
