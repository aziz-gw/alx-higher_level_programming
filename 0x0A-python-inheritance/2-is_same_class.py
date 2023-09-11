#!/usr/bin/python3
"""
Defines a function that if the object is exactly an instance
of the specified class
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class

    Args:
        obj: object to check.
        a_class: specified class

    Returns: True if an obj is exactly an instance of a_class,
    False otherwise
    """
    if type(obj) is a_class:
        return True
    return False
