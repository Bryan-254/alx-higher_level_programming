#!/usr/bin/python3
"""
To JSON string task
Ensure that the import json line is present at top of your script or module.
This should resolve the NameError you're experiencing.
"""
import json


def to_json_string(my_obj):
    """
    the json.dumps() function is part of the json module in Python,
    and it stands for "dump string."

    json.dumps(my_obj): This function takes a Python object (my_obj)
    and returns a JSON-formatted string representing that object.
    """

    return json.dumps(my_obj)
