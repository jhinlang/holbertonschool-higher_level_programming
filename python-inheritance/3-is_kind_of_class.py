#!/usr/bin/python3
"""module docstring for python-inheritance.3-is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class
    or a subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
