#!/usr/bin/python3
'''Define a function.'''


def inherits_from(obj, a_class):
    '''This function specifies if an object is an instance of a class

    Args:
        obj: any object
        a_class: the specified class

    Returns:
        True: if the object is an instance of the class inherited (directly or indirectly) from the specified class or
        False: if not
    '''

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
