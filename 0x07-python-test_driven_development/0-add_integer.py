#!/usr/bin/python3
'''Define an addition function'''


def add_integer(a, b=98):
    '''Returns the sum of a and b.

    Float is typecasted to an integer.

    Raises:
        TyperError: if a or b is not an integer or float
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a+b)
