#!/usr/bin/python3
'''Define a JSON representing function.'''
import json


def to_json_string(my_obj):
    '''Gives JSON representation of an object.

    Args:
        my_obj (str): the object to be converted

    Returns: JSON representation
    '''

    return json.dumps(my_obj)
