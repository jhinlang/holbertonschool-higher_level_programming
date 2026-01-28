#!/usr/bin/python3
'''
Module defining a Square Class
'''


class Square:
    '''Class that defines a square'''

    def __init__(self, size=0):
        '''
        Initialize a Square instance with a given size

        Args:
            size (int): The size of the square
        '''
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
