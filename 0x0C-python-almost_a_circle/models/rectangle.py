#!/usr/bin/python3

"""
Defines a class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises a new Rectangle.

        Args:
            width (int): width of a new Rectangle.
            height (int): height of a new Rectangle.
            x (int): x coordinate of a new Rectangle.
            y (int): y coordinate of a new Rectangle.
            id (int): id  of a new Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter method to retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method to retrieve the x coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method to set the x coordinate."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method to retrieve the y coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method to set the y coordinate."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of a Rectangle instance."""
        return (self.height * self.width)

    def display(self):
        """Prints to the stdout the Rectangle instance with
        the character '#'."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[Rectangle] ({}) {}/{} - {}/{}". format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        Updates a Rectangle.

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
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle.
        """
        return {
                    "id": self.id,
                    "width": self.width,
                    "height": self.height,
                    "x": self.x,
                    "y": self.y
                }
