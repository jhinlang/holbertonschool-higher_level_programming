#!/usr/bin/python3
"""module docstring for python-inheritance.7-base_geometry"""


class BaseGeometry:
    """
    Class BaseGeometry.
    """

    def area(self):
        """
        raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates that value is a positive integer.

        Args:
            name (str): name of value to validate
            value (int): value to validate

        Raises:
            TypeError: if type(value) is not int
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
