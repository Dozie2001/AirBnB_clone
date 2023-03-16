#!/user/bin/python3
"""A Class  for Reviews"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class that instaniates Reviews"""

    place_id = ""
    user_id = ""
    text = ""
