#!/usr/bin/python3
"""A class """

from models.base_model import BaseModel


class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    number_rooms = 0
    description = ""
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    number_bathrooms = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
    price_by_night = 0
