#!/usr/bin/python3

"""
Defines a class Student.
"""


class Student:
    """
    Defines a class student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialises a new Student.

        Args:
            first_name (str): first name a the student.
            last_name (str): last name of a student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) attributes to represent.
        """
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of a Student instance

        Args:
            json (dict): key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
