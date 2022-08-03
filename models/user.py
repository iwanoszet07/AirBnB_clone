#!/usr/bin/python3
"""class User that inherits from BaseModel"""

import models


class User(models.BaseModel):
    """Class to store User info"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
