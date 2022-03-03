#!/usr/bin/python3
"""
Class
    a) Amenity.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class:
        Amenity that inherits from BaseModel.

    Attributes:
        Amenity.name (str):
            Name for amenity.
    """
    name = ""
