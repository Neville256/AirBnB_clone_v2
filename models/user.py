#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    # Specify id as the primary key column
    id = Column(String(60), primary_key=True, nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    # Define the relationships with proper cascade options using a list
    places = relationship('Place', backref='user', cascade=['all', 'delete-orphan'])
    reviews = relationship('Review', backref='user', cascade=['all', 'delete-orphan'])
