#!/usr/bin/python3
"""module docstring for python-inheritance.3-is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    Retourne True si obj est une instance de a_class
    ou d'une classe qui hérite de a_class, sinon False.
    """
    return isinstance(obj, a_class)
