#!/usr/bin/python3
"""A class that serialises instances to a JSON file and deserializes JSON file
 to instances
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


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
            for key, value self.__objects.item():
                dict_storage[key] = value.to_dict()
            json.dump(dict_storage, f)
    
    def reload(self):
        """Deserializes the JSON file to __objects
        -> Only IF it exists!
        """
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review}
        try:
            with open(self.__file.path, mode='r') as f:
                jo = json.load(f)
             for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass
