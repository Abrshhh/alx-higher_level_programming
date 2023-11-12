#!/usr/bin/python3
'''Define a class called Base.'''
import json


class Base:
    '''Represents a Base class.'''

    __nb_objects = 0
    def __init__(self, id=None):
        '''Initialize the class Base.'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Gives JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): The list of dictionaries converted to JSON string.
        Returns:
            the string "[]" : if list_dictionaries is None or empty.
            JSON string (str): if list_dictionaries is not empty or None.
        '''

    if len(list_dictionaries) == 0 or list_dictionaries = None:
        return ("[]")
    else:
        return json.dumps(list_dictionaries)
