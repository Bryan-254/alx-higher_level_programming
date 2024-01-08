#!/usr/bin/python3
"""
Only sub class of task
"""


def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False.

    Check if the type of the object is not equal to the specified class
    (type(obj) != a_class).
    If the object is an instance of the specified class, this condition
    will evaluate to False.

    Check if the type of the object is a subclass of the specified class
    (issubclass(type(obj), a_class)).
    The issubclass function returns True if the first argument is a
    subclass of the second argument.
    """

    return type(obj) != a_class and issubclass(type(obj), a_class)
