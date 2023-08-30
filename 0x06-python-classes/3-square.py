#!/usr/bin/python3

"""Represents a square"""


class Square:
    """Defines a square with private instance attribute size."""

    def __init__(self, size=0):
        """
        Initialises a new square.

        Args:
            size: size of the new square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):

        """Return the current area of the square"""

        return (self.__size * self.__size)
