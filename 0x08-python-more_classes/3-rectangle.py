#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle
"""

class Rectangle:
    """creates class that defines a rectangle
    Attributes:
    empty
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height) if self.width and self.height else 0

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle_str = ""
            for _ in range(self.height):
                rectangle_str += '#' * self.width + '\n'
            return rectangle_str[:-1]
