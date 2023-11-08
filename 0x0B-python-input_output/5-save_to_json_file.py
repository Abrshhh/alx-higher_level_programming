#!/usr/bin/python3
'''Define a function writing an object to a text file.'''


import json
def save_to_json_file(my_obj, filename):
    '''Writes an Object to a text file using JSON representation.'''

    with open(filename, "w") as f:
        json.dumps(my_obj)
