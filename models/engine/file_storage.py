#!/usr/bin/python3
"""This modules defines a class FileStorage that serialises
instances to JSON file and deserialises JSON file instances"""
import models
import json
from os import path


class FileStorage():
    """File storage class."""
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """Returns the dictionary '__objects'"""
        return self.__objects

    def new(self, obj):
        """sets in '__objects'  the 'obj' with key '<obj class name>.id'"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """Serialise '__objects' to the JSON file
        specified by '__file_path'"""
        with open(self.__file_path, "w", encoding = "utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Deserialises the JSON file to '__objects'"""
        if (path.exists(self.__file_path)):
            with open(self.__file_path, "r") as f:
                load_it = json.load(f)
                for k, v in load_it.items():
                    self.__objects[k] = v
        else:
             pass
