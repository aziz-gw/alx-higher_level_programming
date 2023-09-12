#!/usr/bin/python3

"""Defines a class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines a class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Intialises a new Rectangle.

        Args:
            width: width of a new Rectangle.
            height: height of a new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
