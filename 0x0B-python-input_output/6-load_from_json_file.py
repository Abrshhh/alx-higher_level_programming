#!/usr/bin/python3
'''Define a text creating function.'''
import json


def load_from_json_file(filename):
    '''Create an object from JSON file.'''
    with open(filename) as f:
       return json.load(f)
'''
#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
'''
