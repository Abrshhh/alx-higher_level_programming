#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

        for i in range(self.__height):
            if height == 0 or width == 0:
                return ("")
            else:
                print(width * "#")

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns the area of the Rectangle.'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''Calculates the perimeter of the Rectangle
        Returns: 0 if width and/or height are 0 and 2(w+h) if not'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

