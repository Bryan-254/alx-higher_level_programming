#!/usr/bin/python3
"""
Student to JSON task
"""


class Student:
    """Type class of a student"""

    def __init__(self, first_name, last_name, age):
        """
        __init__: This is the constructor method. It initializes
        the instance variables.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        The class also has a method called to_json() which returns
        a dictionary representation of the instance using the
        __dict__ attribute.
        """

        return self.__dict__
