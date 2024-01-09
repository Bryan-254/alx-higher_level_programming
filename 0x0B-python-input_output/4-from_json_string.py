#!/usr/bin/python3
"""
From JSON string to Object task
"""
import json


def from_json_string(my_str):
    """
    json.loads(my_str) is a method in the Python json module
    that is used to parse a JSON string (my_str) and convert
    it into a Python object.

    json.dumps() is for encoding Python objects into JSON strings.
    json.loads() is for decoding JSON strings into Python objects.

    loads: This stands for "load string." It's a method within the
    json module that is used to deserialize a JSON string. The method
    takes a JSON-formatted string as its argument and returns a corresponding
    Python object.
    """

    return json.loads(my_str)
