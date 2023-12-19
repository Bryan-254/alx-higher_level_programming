#!/usr/bin/python3

"""A class that defines a square."""


class Square:
    """Represent a square.

    Methods:
        __init__(self, size=0): Initializes a square with a given size.
        area(self): Returns the current square area.
    """

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)
