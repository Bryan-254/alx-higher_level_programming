#!/usr/bin/python3
"""
Square #2 task
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square class
    """
    def __init__(self, size):
        """
        Instantiation with size
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of the square
        Returns:
            int: The area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """The function to print"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
