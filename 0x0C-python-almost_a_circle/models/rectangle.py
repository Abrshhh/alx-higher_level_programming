#!/usr/bin/python3
'''Define a class called Rextangle.'''


class Rectangle(Base):
    '''Represents a Rectangle that inherits from the class Base.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize the class Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): an integer.
            y (int): an integer.
            id (int): an integer.
        '''

        super().__init__(id) #Call the __init__method of the class Base.
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def get_width(self):
        '''Return the width of the Rectangle.'''
        return self.__width
    @get_width.setter
    def set_width(self, value):
        '''Set the width of the Rectangle.

        Raises:
            TypeError: if width is not integer.
            ValueError: if width <= 0.
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def get_height(self):
        '''Return the height of the Rectangle.'''
        return self.__height
    @get_height.setter
    def set_height(self, value):
        '''Set the height of the Rectangle.

        Raises:
            TypeError: if height is not integer.
            ValueError: if height <= 0.
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def get_x(self):
        '''Return the value of x.'''
        return self.__x
    @get_x.setter
    def set_x(self, value):
        '''Set the value of x.

        Raises:
            TypeError: if x is not integer.
            ValueError: if x < 0.
        '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def get_y(self):
        '''Get the value of y.'''
        return self.__y
    @get_y.setter
    def set_y(self, value):
        '''Set the value of y.

        Raises:
            TypeError: if y is not integer.
            ValueError: if y < 0.
        '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' Returns the area of the Rectangle.'''
        return (self.__width * self.__height)

    def display(self):
        '''Prints A rectangle with the character '#'.'''

        for i in range(self.__height):
            print(self.__width * "#")
