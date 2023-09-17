#!/usr/bin/python3

"""
Defines a base class called Base.
"""
import json


class Base:
    """
    Base class that will be the "base" of all other classes
    in this project
    """

    __nb_objects = 0  # Number of instantiated classes

    def __init__(self, id=None):
        """Initialises a new Base.

        Args:
            id (int): an id of a new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string represntation of list_dictionaries.

        Args:
             list_dictionaries (list): a list of dictionaries
        """
        list_empty = []

        if list_dictionaries is None or list_dictionaries == list_empty:
            return ("[]")

        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): a list of instances who inherits
            from a Base class
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                for obj in list_objs:
                    list_dicts = obj.to_dictionary()
                    file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): a string representing a list of dictionaries.
        """
        list_empty = []
        if json_string is None or json_string is list_empty:
            return list_empty
        return (json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary (dict): a double pointer to a dict
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)

            new.update(**dictionary)
            return (new)

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances; filename must be <Class name>.json.
        If the file doesn't exist, return an empty list, otherwise return
        a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**dictionary) for dictionary
                        in list_dicts]
        except TypeError:
            return []
