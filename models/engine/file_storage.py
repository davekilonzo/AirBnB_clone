#!/usr/bin/python3

import json
import os
from base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = {k: BaseModel(**v) for k, v in json.load(f).items()}
