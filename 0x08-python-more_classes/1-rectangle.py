#!/usr/bin/python3
'''Define a class Rectangle.'''


class Rectangle:
    '''This class represents a Rectangle.'''

    def __init__(self, width=0, height=0):
        '''This function Initializes the class Rectangle.

        Args:
            width: Represents the width of the Rectangle.
            height: Represents the height of the Rectangle.
        '''
        self.__width = width
        self.__height = height

    def width(self, value):
        '''Set the value of width of the Rectangle.'''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def width(self):
        '''Returns: The width of the Rectangle.'''

        return self.__width

    def height(self, value):
        '''Set the value of height of the Rectangle.'''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def height(self):
        '''Returns: The height of the Rectangle.'''

        return self.__height
