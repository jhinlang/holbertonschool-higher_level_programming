#!/usr/bin/python3
"""Module defining a Square Class"""
class Square:
    """Class that defines a Square"""


    def __init__(self, size=0):
        """Initialize a Square instance with a given size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return self.__size ** 2
