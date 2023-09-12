#!/usr/bin/python3

"""
Defines a function that reads a text file (UTF-8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout
    """
    with open("my_file_0.txt", "r", encoding="UTF-8") as f:
        print(f.read())
