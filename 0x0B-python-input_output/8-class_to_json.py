#!/usr/bin/python3
'''Define a JSON serialization function.'''


def class_to_json(obj):
    '''Return dictionary description with simple data structure.'''

    return obj.__dict__
