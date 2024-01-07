#!/usr/bin/python3
"""
function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Check if first_name and last_name are strings
    raise TypeError
    Print the message using f-string
    """

    if not isinstance(first_name, str) or not isinstance(last_name, str):
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
