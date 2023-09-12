#!/usr/bin/python3

"""
Defines a function that writes a string to a text file and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of
    characters written.

    Args:
        filename: file name
        text: text to write

    Returns: number of characters written
    """
    with open(filename, "w", encoding="UTF-8") as f:
        nb_chars = f.write(text)

        return (nb_chars)
