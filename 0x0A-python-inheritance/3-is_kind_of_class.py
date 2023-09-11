#!/usr/bin/python3
"""Defines a class and is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance or inherited instance of a class.

    Args:
        obj: object to check.
        a_class: class of an object

    Returns: True if an obj is an instance of the specified class,
    False, otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
