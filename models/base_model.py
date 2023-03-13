#!/usr/bin/python3
""" This modules defines a base class BaseModel."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ The Base Model"""
    def __init__(self, *args, **kwargs):
        """Initialisations

        Arguments:
            args: This argument is not used
            kwargs: The key-value pair is used to create
                    an instance of BaseModel
        """
        if args:
            raise TypeError

        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'updated_at':
                        setattr(self, k, datetime.fromisoformat(v))
                    elif k == 'created_at':
                        setattr(self, k, datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)
                else:
                    continue
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """String representation of objects"""
        class_name = self.__class__.__name__
        obj_id = self.id
        obj_dict = self.__dict__
        str_rep = "[{}] ({}) {}".format(class_name, obj_id, obj_dict)

        return str_rep

    def save(self):
        """updates the updated_at attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Converts an instance to dictionary"""
        class_name = self.__class__.__name__
        my_dict = {}
        for k, v in self.__dict__.items():
            if k == 'created_at':
                my_dict[k] = self.created_at.isoformat()
            elif k == 'updated_at':
                my_dict[k] = self.updated_at.isoformat()
            else:
                my_dict[k] = v
        my_dict['__class__'] = class_name

        return (my_dict)
