#!/usr/bin/python3

"""
Defines a function that appends a string at the end of a tex file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and returns the number
    of characters added.

    Args:
        filename: file name
        text: string to append

    Returns: number of characters added
    """
    with open(filename, "a", encoding="UTF-8") as f:
        nb_chars_added = f.write(text)

        return (nb_chars_added)
