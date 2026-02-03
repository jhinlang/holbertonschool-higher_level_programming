#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method"""


class BaseGeometry:
    """A base class for geometry-related classes."""

    def area(self):
        """Calculates the area of the geometry.

        Raises:
            Exception: Indicates that the area method is not implemented.
        """
        raise Exception("area() is not implemented")
