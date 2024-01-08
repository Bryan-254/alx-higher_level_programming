#!/usr/bin/python3
"""
function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr))
            or attr.startswith("__")]
