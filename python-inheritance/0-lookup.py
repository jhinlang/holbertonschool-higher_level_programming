#!/usr/bin/python3
"""Module defines a function to lookup attribute and methods of an object"""


def lookup(obj):
    """Prints the list of available attributes and methods of an object.

    Args:
        obj (any): The object to inspect.
    """
    return dir(obj)
