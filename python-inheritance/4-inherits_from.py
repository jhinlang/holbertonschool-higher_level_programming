#!/usr/bin/python3
"""Module that defines a function to check class inheritance"""

def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
