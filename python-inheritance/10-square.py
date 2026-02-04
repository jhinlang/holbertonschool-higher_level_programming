#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initializes a Square instance with size.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
