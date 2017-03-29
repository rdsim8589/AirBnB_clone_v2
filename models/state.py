#!/usr/bin/python3
from models.base_model import BaseModel, Base, Table, Column, String
import models
from sqlalchemy.orm import relationship, backref
from os import getenv
"""
state module
    contain
        State class
"""


class State(BaseModel, Base):
    """
    This is the State class
    """
    if getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""
        @property
        def cities(self):
            """
            return a dictionary of the city and the city id
            """
            city_state_objs = []
            for city_obj in models.storage.all("City").values():
                if self.id == city_obj.state_id:
                    city_state_objs.append(city_obj)
            return city_state_objs


    def __init__(self, *args, **kwargs):
        """
        initializes from BaseModel Class
        """
        super(State, self).__init__(*args, **kwargs)
