#!/usr/bin/python3
'''Define a function.'''


def is_kind_of_class(obj, a_class):
    '''This function specifies if the object is an instance of,
    or if the object is an instance of a class that inherited from, the specified class.

    Args:
        obj: the object.
        a_class: the specified class.

    Returns:
        True or False if the object fullfuill the requirement or not
    '''

    if isinstance(obj, a_class):
        return True
    else:
        return False
