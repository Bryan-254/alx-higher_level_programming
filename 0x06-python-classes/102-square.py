#!/usr/bin/python3

"""A class for square"""


class Square:
    """
    This class defines a square.

    Attributes:
        __size (float or int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a Square instance.
        size(self): Getter for the size attribute.
        size(self, value): Setter for the size attribute.
        area(self): Calculates and returns the area of the square.
        __eq__(self, other): Checks if two squares have equal areas.
        __ne__(self, other): Checks if two squares have unequal areas.
        __lt__(self, other): Checks if the area of the current square is
        less than the area of another square.
        __le__(self, other): Checks if the area of the current square is
        less than or equal to the area of another square.
        __gt__(self, other): Checks if the area of the current square is
        greater than the area of another square.
        __ge__(self, other): Checks if the area of the current square is
        greater than or equal to the area of another square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Parameters:
            size (float or int): The size of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Parameters:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two squares have equal areas.

        Parameters:
            other (Square): Another Square instance.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Checks if two squares have unequal areas.

        Parameters:
            other (Square): Another Square instance.

        Returns:
            bool: True if areas are unequal, False otherwise.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Checks if the area of the current square is less than
        the area of another square.

        Parameters:
            other (Square): Another Square instance.

        Returns:
            bool: True if the current square's area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Checks if the area of the current square is less than
        or equal to the area of another square.

        Parameters:
            other (Square): Another Square instance.

        Returns:
            bool: True if current square's area is < or equal, else False.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        Checks if the area of the current square is greater than
        the area of another square.

        Parameters:
            other (Square): Another Square instance.

        Returns:
            bool: True if the current square's area is greater, else False
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Checks if the area of the current square is greater than
        or equal to the area of another square.

        Parameters:
            other (Square): Another Square instance.

        Returns:
            bool: True if the current square's area is greater than
            or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
