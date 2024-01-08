#!/usr/bin/python3
"""
This involves defining function to check if you can add attribute
"""


def add_attribute(obj, name, value):
    """
    checks if can add atrribute

    The function checks if the object has a __dict__ attribute,
    which indicates that it allows adding new attributes.
    If the object allows it, the function uses setattr to add
    the attribute with the specified name and value.
    """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
