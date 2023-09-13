#!/usr/bin/python3

"""
Defines a function append_after that inserts a line of text to a file
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string

    Args:
        filename (str): name of the file.
        search_string (str): string to search for within the file.
        new_string (str): string to insert.
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w", encoding="UTF-8") as w:
        w.write(text)
