#!/usr/bin/python3
"""A class that serialises instances to a JSON file and deserializes JSON file
 to instances
"""

import json
from models.base_model import BaseModel



class FileStorage():
    """serializes instances to a JSON file and
       deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
    
    def save(self):
        """Serializes __objects to the JSON file(path: __file_path)"""
        with open(self.__file_path, mode='w') as f:
            dict_storage = {}
            for key, value  in self.__objects.item():
                dict_storage[key] = value.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        -> Only IF it exists!
        """
        classes = {
            'BaseModel': BaseModel}
        try:
            with open(self.__file.path, mode='r') as f:
                jo = json.load(f)
                for key in jo:
                    self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass
