#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """It represents a Square"""

    def __init__(self, size=0):
        """ """
        self.__size = size
    def get_size(self):
        """ """
        return (self.__size)
    def set_size(self, value):
        """ """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """ """
        return (self.__size * self.__size)
