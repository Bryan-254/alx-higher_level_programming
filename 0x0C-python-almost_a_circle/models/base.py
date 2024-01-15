#!/usr/bin/python3
"""
Base Module
"""
import json
import csv
import turtle


class Base:
    """
    Base class

    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.
        Use this method to convert lists of dictionaries to JSON strings.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            list_objs = []

        file_name = cls.__name__ + ".json"

        with open(file_name, mode="w", encoding="utf-8") as file:
            json_str = cls.to_json_string([obj.to_dictionary()
                                           for obj in list_objs])
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            """Creating a dummy Rectangle instance"""
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            """Creating a dummy Square instance"""
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    def update(self, *args, **kwargs):
        """
        Updates instance attributes with the values passed as
        arguments or keyword arguments.
        """
        if args:
            attrs = ["id", "width", "height", "size", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.

        The Base class now has a class method load_from_file that reads the
        JSON string from the file <Class name>.json and returns a list of
        instances created using the create method. If the file doesn't exist,
        it returns an empty list.
        """
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, mode="r", encoding="utf-8") as file:
                json_str = file.read()
                dict_list = cls.from_json_string(json_str)
                return [cls.create(**d) for d in dict_list]
        except FileNotFoundError:
            return []
