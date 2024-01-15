#!/bin/usr/python3
"""
Module for square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Type class of a square inherited from rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square attributes.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Convert the Square attributes to a dictionary.

        Returns:
            dict: A dictionary containing the Square attributes.
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
