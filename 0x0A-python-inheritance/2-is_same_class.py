#!/usr/bin/python3
"""
Exact same object task
"""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.

    Function checks if the type of the given object (type(obj)) is
    exactly equal to the specified class (a_class)

    If they are the same, it returns True; otherwise, it returns False.
    """

    return type(obj) is a_class
