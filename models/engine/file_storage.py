#!/usr/bin/python3
"""
Class
    a) FileStorage.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class:
        FileStorage that serializes instances to a JSON file
        and deserializes JSON file to instances

    Attributes:
        FileStorage.__file_path (str):
            Path to the JSON file.
        FileStorage.__objects (dict):
            Store all objects by <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Method:
            Get de dictionary __objects.

        Return:
            The dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Method:
            Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj (object):
                Object of create dictionary
        """
        key = "{0}.{1}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Method:
           Serializes __objects to the JSON file (path: __file_path)
        """
        # info!: [objs_dict] Dictionary contains all dict of the objects
        objs_dict = self.__objects.copy()

        # info!: Serializable objects and Save in Json file
        for key, obj in self.__objects.items():
            objs_dict[key] = obj.to_dict()
        # note!: Use mode W is correct or A?
        with open(self.__file_path, mode="w") as file_json:
            file_json.write(json.dumps(objs_dict))

    def reload(self):
        """
        Method:
            Deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists).
        """
        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        try:
            with open(self.__file_path, mode="r") as file_json:
                # info!: values contain of dictionary attributes of the object
                for key, values in json.load(file_json).items():
                    class_name = values["__class__"]
                    self.new(class_dict[class_name](**values))
        except Exception:
            pass
