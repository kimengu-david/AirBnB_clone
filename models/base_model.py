#!/usr/bin/python3

"""Defines class basemodel."""

import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Define common attributes and methods of the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialized a new BaseModel.
        Args:
            *args (any): Unused.
            **kwargs (dict): Key-value pairs of dictionary attributes.
        """
        self.id = str(uuid4())
        self.updated_at = datetime.today()
        self.created_at = datetime.today()
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "updated_at" or key == "created_at":
                        value = datetime.strptime(value, d_format)
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """ updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """  returns a dictionary containing all keys/values
             of __dict__ of the instance
        """
        c_dict = self.__dict__.copy()
        c_dict["__class__"] = self.__class__.__name__
        c_dict["created_at"] = self.created_at.isoformat()
        c_dict["updated_at"] = self.updated_at.isoformat()
        c_dict["id"] = str(uuid4())
        return c_dict

    def __str__(self):
        """Prints the dictionary representation of the BaseModel instance"""

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
