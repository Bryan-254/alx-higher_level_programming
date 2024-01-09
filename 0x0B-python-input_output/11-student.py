#!/usr/bin/python3
"""
Student to disk and reload task
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance with the given
        first name, last name, and age

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json(self, attrs=None): This method retrieves a
        dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        reload_from_json(self, json): This method replaces all
        attributes of the Student instance based on the provided
        dictionary (json).
        """
        for key, value in json.items():
            setattr(self, key, value)
