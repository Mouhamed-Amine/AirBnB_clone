#!/usr/bin/python3

"""
this file represents the Ser of instance to json file and vice versa

"""
import json
from models.base_model import BaseModel

class FileStorage():


    __file_path=""
    __objects= {}

    def all(self):

        return FileStorage.__objects
    def new(self, obj):
    
        key= "{}.{}".format(type(obj).__name__.obj.id)
        FileStorage.__objects[key]= obj

    def save(self):

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {k: v.to_dict() for x,v in FileStorage.__objects.items()}, f)
    def reload(self):
        with open(FileStorage.__file_path, 'r') as f:
            deserialized = None

            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return
