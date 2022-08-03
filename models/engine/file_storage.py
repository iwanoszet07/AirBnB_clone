#!/usr/bin/python3
"""Store first object"""

import models
import json


def models_obj_hook(o_dict):
    """imports BaseModel from models and returns dict"""
    try:
        cls = o_dict['__class__']
    except KeyError:
        return o_dict
    else:
        try:
            return getattr(models, cls)(**o_dict)
        except AttributeError:
            return o_dict


class FileStorage:
    """created private class attributes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary"""
        return self.__objects

    def new(self, obj):
        """sets the obj with key"""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w') as f:
            jdict = {}
            for name, obj in self.__objects.items():
                jdict[name] = obj.to_dict()
            json.dump(jdict, f)

    def reload(self):
        """deserializes the JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f, object_hook=models_obj_hook)
        except:
            pass
