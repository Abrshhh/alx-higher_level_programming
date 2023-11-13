#!/usr/bin/python3
'''Define a class called Square that inherits from the class Rectangle.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Represents a Square.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initializes the class Square.'''

        super().__init__(size, size, x, y, id)

    def __Str__(self):
        return f"([Square] {id} {self.__x}/{self.__y} - {self.__width})"

    @property
    def get_size(self):
        '''Return the size of the Square.'''
        return self.size
    @get_size.setter
    def set_size(self, value):
        '''Set the size of the Square.

        Raises:
            TypeError: if size is not integer.
            ValueError: if size <= 0.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if width <= 0:
            raise ValueError("size must be > 0")
        self.size = value

    def to_dictionary(self):
        '''Return a dictionary from attributes of the class Square.'''

        return dict(id = self.id, size = self.size, x = self.get_x, y = self.get_y)
