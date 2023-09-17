#!/usr/bin/python3
"""
Defines a class Square that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialises attributes of a square.

        Args:
            size (int): size of a new square.
            x (int): x coordinate of a new square
            y (int): y coordinate of a new square
            id (int): id of a new square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns [Square] (<id>) <x>/<y> - <size>
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width, self.height))

    @property
    def size(self):
        """Getter method to retrieve the size of a square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates a square.

        Args:
            *args (ints): variable number of attributes
                          1st arg is the id attribute
                          2nd arg is the width attribute
                          3rd arg is the height attribute
                          4th arg is the x attribute
                          5th arg is the y attribute
            **kwargs (dicts): new key/value pairs of attributes
        """
        if args and len(args) != 0:
            a = 0

            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
                    "id": self.id,
                    "size": self.width,
                    "x": self.x,
                    "y": self.y
                }
