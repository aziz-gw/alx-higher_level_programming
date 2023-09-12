#!/usr/bin/python3
"""Defines a function that adds attributes to an object."""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: object to add an attribute to.
        att: name of the attribute to add to obj.
        value: value of an attr.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
