#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """It represents a Square."""

    def __init__(self, size=0):
        """Initialize the class Square.

        Args:
            size: size of the square."""
        self.__size = size

    @property
    def size(self):
        """Returns the size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set new size to the class Square.

        Args:
            value: new size of the Square."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return value

    def area(self):
        """Calculates the area of the square."""
        return (self.__size * self.__size)
