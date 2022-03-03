#!/usr/bin/python3
"""
Class
    a) Place.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class:
        Place that inherits from BaseModel.

    Attributes:
        Place.city_id (str):
            ID city for place.
        Place.user_id (str):
            ID user for place.
        Place.name (str):
            Name for place.
        Place.description (str):
            Description for place.
        Place.number_rooms (int):
            Number Rooms for place.
        Place.number_bathrooms (int):
            Number Bathrooms for place.
        Place.max_guest (int):
            Max Guest for place.
        Place.price_by_night (int):
            Price By Night for place.
        Place.latitude (float):
            Latitude Night for place.
        Place.longitude (float):
            Longitude Night for place.
        Place.amenity_ids (list:str)
            List of ID Amenity for place.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
