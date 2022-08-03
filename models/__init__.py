#!/usr/bin/python3
"""Import FileStorage and read existing data into `storage` variable"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

class_dict = {
    'BaseModel': BaseModel,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review,
    'User': User
}

storage = FileStorage()
storage.reload()
