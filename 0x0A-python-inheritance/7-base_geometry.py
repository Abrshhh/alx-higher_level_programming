#!/usr/bin/python3
'''Define a class called BaseGeometry.'''


class BaseGeometry:
    '''Represents a Base Geometry.'''

    def area(self):
        '''Not implemented'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''A method that validates value.

        Args:
            name (str): name
            value (int): value

        Returns:
            TypeError: if name is not integer.
            ValueError: if name is not >= 0.
        '''

    if not isinstance(value, int):
        raise TypeError("<name> must be an integer")
    if value < 0:
        raise ValueError("<name> must be greater than 0")
