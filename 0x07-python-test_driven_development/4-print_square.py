#!/usr/bin/python3
'''Define a function printing a square with #.'''


def print_square(size):
    '''This function prints a square formed from "#".

    Args:
        size (int): the size length of the square.

    raises:
        TypeError: if size is not integer or size is a float and it is < 0.
        ValueError: if size is < 0.
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print(size * "#")
