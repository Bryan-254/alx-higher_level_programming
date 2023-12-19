#!/usr/bin/python3

class Square:
    """
    Square class represents a square with a size and position.

    Attributes:
        size (int): The size of the square.
        position (tuple): Position of square as tuple of 2 positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If the position is not tuple of two positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            any(i < 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string representation of the square.
        """
        output = ""
        if self.size == 0:
            return output

        for _ in range(self.position[1]):
            output += "\n"

        for _ in range(self.size):
            output += " " * self.position[0] + "#" * self.size + "\n"

        return output.rstrip()
