#!/usr/bin/python3
"""
From JSON string to Object task
"""
import json


def save_to_json_file(my_obj, filename):
    """
    the json.dump function is used to serialize the my_obj
    and write it to the specified file using the with statement.

    The with statement ensures that the file is properly closed
    after writing, even if an exception occurs during the process.

    Serialization is the process of converting a data structure or
    object into a format that can be easily stored, transmitted,
    or reconstructed.

    In the current context with the json.dump function, serialization refers
    to the process of converting a Python object (such as a dictionary, list,
    or other data structure) into a JSON (JavaScript Object Notation) string.
    """

    with open(filename, 'w') as file:
        json.dump(my_obj, file)
