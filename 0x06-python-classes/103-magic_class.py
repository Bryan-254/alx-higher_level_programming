#!/usr/bin/python3
import math

class MagicClass:
    """
    A magical class for performing calculations based on a radius.

    Attributes:
    - __radius (int or float): The radius of the magical circle.

    Methods:
    - __init__(self, radius): Initializes the MagicClass instance.
    - area(self): Calculates and returns the area of the magical circle.
    - circumference(self): Returns the circumference of the magical circle.
    """

    def __init__(self, radius):
        """
        Initializes the MagicClass instance with a given radius.

        Parameters:
        - radius (int or float): The radius of the magical circle.

        Raises:
        - TypeError: If the provided radius is not an int or a float.
        """
        self.__radius = 0  # Initialize with default value

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the magical circle.

        Formula: area = π * radius^2

        Returns:
        - float: The area of the magical circle.
        """
        return self.__radius**2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the magical circle.

        Formula: circumference = 2 * π * radius

        Returns:
        - float: The circumference of the magical circle.
        """
        return 2 * math.pi * self.__radius
