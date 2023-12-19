#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            any(i < 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        output = ""
        if self.size == 0:
            return output

        for _ in range(self.position[1]):
            output += "\n"

        for _ in range(self.size):
            output += " " * self.position[0] + "#" * self.size + "\n"

        return output.rstrip()
