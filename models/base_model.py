#!/usr/bin/python3

import uuid
from datetime import datetime
import storage

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        self.storage.save()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
    def __init__(self, *args, **kwargs):
        if kwargs: # if there are keyword arguments

            for key in kwargs:  # for each key in the dictionary
                value = kwargs[key]  # get the value for this key
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")  # convert string to datetime
                elif key == "__class__":
                    continue  # skip this key
                setattr(self, key, value)  # set the attribute on the instance
        else:  # if there are no keyword arguments
            self.id = str(uuid.uuid4())  # generate a unique ID
            self.created_at = self.updated_at = datetime.now()
        if not kwargs:
            self.storage.new(self)
