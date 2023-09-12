#!/usr/bin/python3
"""Defines a class Square that inherits from a class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines a class Square that inherits from a class Rectangle
    """

    def __init__(self, size):
        """Initialises a new square.

        Args:
            size: size of a new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
