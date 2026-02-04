#!/usr/bin/python3
"""module docstring for python-inheritance.4-inherits_from"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class
    that inherits (directly or indirectly) from a_class,
    but is NOT an instance of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
