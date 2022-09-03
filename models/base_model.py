#!/usr/bin/python3
"""Module base_model
Defines attributes/methods common to other classes."""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """Base class of the object hierachy."""

    def __init__(self, *args, **kwargs):
        """Initialize Base instance.
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                format = "%Y-%m-%dT%H:%M:%S.%f"
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], format)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], format)
                elif key != "__class__":
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns string representation of the object"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/value of __dict__
        of the instance"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
