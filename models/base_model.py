#!/usr/bin/python3
"""
Class
    a) BaseModel.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Class:
        BaseModel that defines all common attributes/methods
        for other classes.

    Attributes:
        id (str):
            ID unique of object.
        created_at (datetime):
            Datetime when an instance is created.
        updated_at (datetime):
            Datetime when an instance is created, and it will be updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Construct (replace):
                BaseModel object.

        Args:
            *args (tuple):
                Non-keyword variable length argument list.
            **kwargs (dict):
                Keyword variable length of arguments.
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Method (replace):
            Represents the class objects as a string in format.

        Return:
            String in  format '[<class name>] (<self.id>) <self.__dict__>'.
        """
        class_str = "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
        return class_str

    def save(self):
        """
        Method:
            Update auditory date and save change.
        """
        # note!: According to review it should be datetime.utcnow().
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Method:
            Generate dictionary of the class.

        Return:
            A dictionary containing all keys/values of __dict__ the instance.
        """
        class_dict = self.__dict__.copy()
        class_dict['__class__'] = self.__class__.__name__
        class_dict['created_at'] = class_dict['created_at'].isoformat()
        class_dict['updated_at'] = class_dict['updated_at'].isoformat()
        return class_dict
