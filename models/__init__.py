#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import models
import os
#from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.base_model import BaseModel


classes = {"User": User, "City": City, "Place": Place,
           "Amenity": Amenity, "Review": Review,
           "State": State, "BaseModel": BaseModel}

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
#    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
#    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()

