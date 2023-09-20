#!/usr/bin/python3
""" Amenity Module for HBNB project """
import os
from sqlalchemy import Column, String, Integer  # Import Integer type
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Represents an amenity data set."""
    __tablename__ = 'amenities'

    # Define 'id' as the primary key column
    id = Column(Integer, primary_key=True, nullable=False, unique=True)

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        pass
    else:
        name = ''
