#!/usr/bin/python3
"""Module file_storage
Storage system for object utilizing JSON format."""

import json
import os


class FileStorage():
    """Serializes instances to a JSON file and deserializes JSON file
    to instance."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            o_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(o_dict, f)

    def reload(self):
        """Deserializes JSON file to __objects"""
        from models.base_model import BaseModel

        file = FileStorage.__file_path
        if os.path.isfile(file):
            with open(file, 'r', encoding="utf-8") as f:
                o_dict = json.load(f)
                o_dict = {k: BaseModel(**v) for k, v in o_dict.items()}
                FileStorage.__objects = o_dict
