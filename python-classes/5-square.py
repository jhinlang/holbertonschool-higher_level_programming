#!/usr/bin/python3
"""
This module defines a Square class with size validation, area calculation,
and a method to print the square using '#' characters.
"""


class Square:
    """
    Represents a square with size validation, area calculation, and printing.
    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using #"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                print("#" * self.__size)
