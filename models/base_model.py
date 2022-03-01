#!/usr/bin/python3
""" Class
        a) BaseModel.
"""
import uuid
from datetime import datetime


class BaseModel:
    """ Class:
            BaseModel that defines all common attributes/methods
            for other classes
    """

    def __init__(self):
        """ Construct (replace):
                BaseModel object.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Method (replace):
                Represents the class objects as a string in format
            Return:
                String in  format '[<class name>] (<self.id>) <self.__dict__>'
        """
        class_str = ""
        class_str += "[" + self.__class__.__name__ + "] "
        class_str += "(" + self.id + ") "
        class_str += self.__dict__
        return class_str
