#!/usr/bin/python3

"""
Defines a JSON representation of an object(string).
"""
import json


def to_json_string(my_obj):
    """"
    Returns the JSON representation of an object (string).

    Args:
        my_obj: object to serialise
    """
    return (json.dumps(my_obj))
