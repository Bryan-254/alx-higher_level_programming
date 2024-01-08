#!/usr/bin/python3
"""
Integer validator task
"""


class BaseGeometry:
    """
    BaseGeometry class
    """

    def area(self):
        """
        This is the area function
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This is the function that validates integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
