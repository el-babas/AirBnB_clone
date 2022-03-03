#!/usr/bin/python3
"""
Class
    a) City.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class:
        City that inherits from BaseModel.

    Attributes:
        City.state_id (str):
             ID State for city.
        City.name (str):
            Name for city.
    """
    state_id = ""
    name = ""
