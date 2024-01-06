#!/usr/bin/python3
"""
Function that returns the add two integers
"""


def add_integer(a, b=98):
    """ Adds two integers
    a and b must be integers if they are floats
    it casts them, it returns the sum of a and b.
    """

    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if b is None or (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
