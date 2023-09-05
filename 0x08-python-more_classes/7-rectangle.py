#!/usr/bin/python3

"""
Defines a rectangle
"""


class Rectangle:
    """
    Defines a rectangle

    Attributes:
            number_of_instances: number of Rectangle instances.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """Initialises a new Rectangle.

        Args:
            width: width
            height: height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter method to retrieve the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method to set the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method to retrieve the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method to set the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of a Rectangle. """
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of a Rectangle. """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ Returns the printable representation of a Rectangle
            a prints a rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            [rectangle.append(str(self.print_symbol))
             for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """ Returns a string representation of a Rectangle. """
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
