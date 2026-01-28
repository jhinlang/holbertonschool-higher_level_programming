#!/usr/bin/python3
'''
Module defining a Square Class
'''


class Square:
   '''
    Represents a square with size validation.
    Attributes:
        __size (int): The size of the square.
    '''

    def __init__(self, size=0):
        '''
        Initialize a Square instance with a given size

        Args:
            size (int): The size of the square
            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is negative.
        '''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
