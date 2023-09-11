#!/usr/bin/python3
"""Defines an inherited function inherits_from"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj: object to check.
        a_class: class of an object

    Returns: True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class ;
    otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
