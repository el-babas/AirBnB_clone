#!/usr/bin/python3
"""
Class
    a) Review.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class:
        Review that inherits from BaseModel.

    Attributes:
        Review.place_id (str):
             ID Place for Review.
        Review.user_id (str):
             ID User for Review.
        Review.text (str):
            Content, more information, for Review.
    """
    place_id = ""
    user_id = ""
    text = ""
