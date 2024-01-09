#!/usr/bin/python3
"""
Class to JSON task
"""


def class_to_json(obj):
    """
    return dict

    return obj.__dict__ is used to retrieve the
    dictionary representation of an object's attributes.
    """
    return obj.__dict__
