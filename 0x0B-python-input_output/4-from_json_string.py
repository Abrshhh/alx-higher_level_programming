#!/usr/bin/python3
'''Define a JSON representing function.'''
import json


def from_json_string(my_str):
    ''' Gives python representation of a JSON string.

    Args:
        my_obj (str): the string to be converted to python object type

    Returns: python representation
    '''

    return json.loads(my_str)
