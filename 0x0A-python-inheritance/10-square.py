#!/usr/bin/python3
"""
Square #1 task
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square class
    """
    def __init__(self, size):
        """
        Instantiation of Square with size
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of the rectangle
        Returns:
            int: The area of the rectangle
        """
        return self.__size * self.__size
