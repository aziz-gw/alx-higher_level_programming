#!/usr/bin/python3
"""Represents a class MagicClass."""

import math


class MagicClass:
    """"
    Defines a MagicClass matching exactly the provided bytecode.
    """

    def __init__(self, radius=0):
        """Initialises a MagicClass.

        Arg:
             radius: radius of a new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns the circumference of a MagicClass."""
        return (2 * math.pi * self.__radius)
