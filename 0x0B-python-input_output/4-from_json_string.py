#!/usr/bin/python3

"""
Defines an object (Python data structure) represented a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string

    Args:
        my_str: object to deserialise

    Returns: an object represented by a JSON string
    """
    return (json.loads(my_str))
