#!/usr/bin/python3
'''Define a text creating function.'''
import json


def load_from_json_file(filename):
    '''Create an object from JSON file.'''

    with open(filename) as f:
       return json.load(f)
