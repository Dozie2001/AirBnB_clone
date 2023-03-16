#!/usr/bin/python3
"""A model that implements BaseModel"""


from datetime import datetime
from uuid import uuid4


class BaseModel:
    def __init__(self, *args,  **kwargs):
        # Don't understand this
        if not kwargs:
            # Don't understand yet
            from models.__init__ import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            del kwargs["__classes__"]
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__.update(kwargs)

    def __str__(self):
        """
        Returns the string representation of BaseModel object.
        [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Update the updated_at with the current date_time"""
        from models.__init__ import storage
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all key/values __dict__
          * Using self.__dict__, only instance attributes set will be returned
          * a key __class__ must be added to this

          dictionary with the class name of the object

          * created_at and updated_at must be converted
          to string object in ISO format
        """

        my_dict = self__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        for key, values in self.__dict__.items():
            if key in (created_at, updated_at):
                value = self.__dict__[key].isoformat()
                my_dict[key] = value
        return my_dict
