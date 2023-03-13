#!/usr/bin/python3
"""This modules defines the initialisation of the package."""
from .engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
