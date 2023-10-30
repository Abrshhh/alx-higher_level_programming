#!/usr/bin/python3
'''Define a class Rectangle.'''


class Rectangle:
    '''This class represents a Rectangle.'''

    def __init__(self, width=0, height=0):
        '''This function Initializes the class Rectangle.

        Args:
            width(int): Represents the width of the Rectangle.
            height(int): Represents the height of the Rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Returns: The width of the Rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set the value of width of the Rectangle.'''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Returns: The height of the Rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set the value of height of the Rectangle.'''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
