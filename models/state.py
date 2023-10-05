#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, String, Integer  # Import Integer for primary key
from sqlalchemy.orm import relationship
import os
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # Unconditional relationship definition
    cities = relationship(
        'City',
        cascade='all, delete, delete-orphan',
        backref='state')

    def __init__(self, *args, **kwargs):
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.name = ''
        super().__init__(*args, **kwargs)
