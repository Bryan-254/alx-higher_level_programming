#!/usr/bin/python3
"""
Full Rectangle task
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A representation of a rectangle
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of the rectangle
        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
