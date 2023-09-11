#!/usr/bin/python3

"""
Defines MyList class which is a subclass of the built-in
class list
"""


class MyList(list):
    """
    Define MyList class that inherits from list built-in object
    """

    def print_sorted(self):
        """
        Prints a sorted list in ascending order
        """
        print(sorted(self))
