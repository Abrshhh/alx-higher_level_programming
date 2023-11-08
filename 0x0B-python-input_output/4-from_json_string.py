#!/usr/bin/python3
'''Define a JSON representing function.'''


import json
def to_json_string(my_obj):
    ''' Gives python representation of a JSON object.

    Args:
        my_obj (str): the object to be converted to python type.

    Returns: python representation.
    '''

    return json.loads(my_obj)
