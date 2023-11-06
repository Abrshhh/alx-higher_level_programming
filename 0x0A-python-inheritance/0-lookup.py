#!/usr/bin/python3
'''Define a function returning attribute and method.'''


def lookup(obj):
    ''' Returns list of attribute and methods of obj.

    Args:
        obj: any object
    '''
    my_list = (dir(obj))
    return my_list
