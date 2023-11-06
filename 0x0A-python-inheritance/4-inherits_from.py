#!/usr/bin/python3
'''Define a function.'''


def inherits_from(obj, a_class):
    '''This function specifies if an object is an instance of a class.

    Args:
        obj (any): any object.
        a_class (type): the specified class.
    Returns:
        True: if the object is an instance of the class inherited (directly or indirectly) from the specified class.
        False: if not.
    '''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
