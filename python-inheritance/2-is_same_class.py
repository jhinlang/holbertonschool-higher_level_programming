#!/usr/bin/python3
"""module docstring for python-inheritance.2-is_same_class"""


def is_same_class(obj, a_class):
    """
    Retourne True si obj est exactement une instance de a_class,
    sinon retourne False.
    """
    return type(obj) is a_class
