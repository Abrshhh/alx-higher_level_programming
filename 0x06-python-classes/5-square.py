#!/usr/bin/python3
'''create a class called Square'''

class Square:
    '''This class represents a Square.'''

    def __init__(self, size=0):
        ''' Initializes the class Square.'''

        self.__size = size

    @property
    def size(self):
        '''This function returns the size of the Square.'''

        return self.__size

    @property.setter
    def size(self, value):
        '''This function sets new size to the Square.'''

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return value

    def area(self):
        '''This function returns area of the Square.'''

        return (self.__size ** 2)

    def my_print(self):
        '''Prints the area of the Square with string '#' '''
        if self.__size == 0:
            print "\n"
        else:
            for i in range(self.__size):
                print(self.__size * "#")
