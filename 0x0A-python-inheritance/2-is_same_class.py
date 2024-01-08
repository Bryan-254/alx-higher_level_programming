#!/usr/bin/python3
"""
Exact same object task
"""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.

    The isinstance() function already returns a boolean value (True or False),
    so you don't need to explicitly return True or False.

    You can directly return the result of the isinstance() check.
    """

    return isinstance(obj, a_class)

a = 1

if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
