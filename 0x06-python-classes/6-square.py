#!/usr/bin/python3

class Square:
    """Defines a square with private instance attributes: size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square.

        Args:
            size: size of the new square.
            position: position of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2 or \
           not all(isinstance(coord, int) for coord in position) or \
           not all(coord >= 0 for coord in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Return the current area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Getter method to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method to retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(coord, int) for coord in value) or \
           not all(coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square pattern using '#'"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
