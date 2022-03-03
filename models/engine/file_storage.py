#!/usr/bin/python3
"""
Class
    a) FileStorage.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Class:
        FileStorage that serializes instances to a JSON file
        and deserializes JSON file to instances

    Attributes:
        __file_path (str):
            <ca> Path to the JSON file.
        __objects (dict):
            <ca> Store all objects by <class name>.id.
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
        objs_dict = dict()

        # info!: Serializable objects and Save in Json file
        if self.__objects is not None and self.__objects:
            for key, obj in self.__objects.items():
                objs_dict[key] = obj.to_dict()
                with open(self.__file_path, mode="w") as file_json:
                    json.dump(objs_dict, file_json)

    def reload(self):
        """
        Method:
            Deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists).
        """
        class_dict = {"BaseMode": BaseModel}
        try:
            with open(self.__file_path, mode="r") as file_json:
                # info!: values contain of dictionary attributes of the object
                for key, values in (json.load(file_json)).items:
                    class_name = values["__class__"]
                    self.new(class_dict[class_name](**values))
        except BaseException:
            pass
