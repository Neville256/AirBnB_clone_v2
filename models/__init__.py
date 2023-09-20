#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import models
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

"""A unique FileStorage/DBStorage instance for all models."""
def initialize_storage():
    storage.reload()
