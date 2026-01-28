#!/usr/bin/python3
"""Simple square module.

This module contains the definition of the Square class,
which keeps the size of a square in a private attribute.
"""


class Square:
    """Represents a square.

    This class stores the size of the square in a private attribute.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size
    @property
    def size(self):
        """int: Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the area of the square.

        Returns:
            int: The current area of the square.
        """
        return self.__size ** 2
