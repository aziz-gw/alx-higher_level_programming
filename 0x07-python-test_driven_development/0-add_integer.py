#!/usr/bin/python3

"""
Defines a function called `add_integers` that add two numbers (a nd b) and returns the result of those numbers.
a and be must be integers or floats, otherwise a TypeError exeception will be raised, with a message 'a must be an integer or b must be an integer`.

"""


def add_integer(a, b=98):
    """
    Returns the result of addition of a and b
    """

    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
