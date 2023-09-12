#!/usr/bin/python3

"""Defines a class BaseGeometry"""


class BaseGeometry:
    """
    Define a class BaseGeometry
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value

        Args:
            name: name of the parameter.
            value: value to validate.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
