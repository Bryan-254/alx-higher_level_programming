#!/usr/bin/python3
"""
Rectangle task
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class for rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        self.__width = 0  # Initializing to 0, will be validated later
        self.__height = 0  # Initializing to 0, will be validated later
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
