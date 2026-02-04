#!/usr/bin/python3
"""module docstring for python-inheritance.2-is_same_class"""


def is_same_class(obj, a_class):
    """
    Return True if obj is exactly an instance of a_class,
    otherwise return False.
    """
    return type(obj) is a_class
