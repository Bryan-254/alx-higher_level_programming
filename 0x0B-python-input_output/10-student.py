#!/usr/bin/python3
"""
Student to JSON with filter task
"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation function for Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of an object or
        a dictionary representation of all string attributes
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
