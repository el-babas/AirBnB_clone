#!/usr/bin/python3
"""
Class
    a) User.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class:
        User that inherits from BaseModel.

    Attributes:
        User.Email (str):
            Email for user.
        User.password (str):
            Password for user.
        User.first_name (str):
            First Name for user.
        User.last_name (str):
            Last Name for user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
