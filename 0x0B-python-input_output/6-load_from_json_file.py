#!/usr/bin/python3
"""
Create object from a JSON file task
"""
import json


def load_from_json_file(filename):
    """
    This function uses the with statement to open the file, read its contents,
    and then use json.loads to parse the JSON data and convert it into a
    Python object.

    The resulting object is then returned.
    """

    with open(filename, 'r') as file:
        json_data = file.read()
        obj = json.loads(json_data)
        return obj
