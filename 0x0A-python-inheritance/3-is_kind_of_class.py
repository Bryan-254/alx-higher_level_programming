#!/usr/bin/python3
"""
Same class or inherit from task
"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.

    The isinstance() function already returns a boolean value (True or False),
    so you don't need to explicitly return True or False.

    You can directly return the result of the isinstance() check.
    """

    return isinstance(obj, a_class)
