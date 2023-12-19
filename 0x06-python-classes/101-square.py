#!/usr/bin/python3


class Square:
    """
    creates square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        initializes square

        Args:
            size: size of side of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        finds size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        validates size is an integer that is greater than zero
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        finds area of square

        Returns:
            area of square
        """
        return self.__size ** 2

    @property
    def position(self):
        """
        finds position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets position

        Args:
            value: position of the square
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """
        prints square with character #
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.position[1]):
            print("")
        for i in range(self.__size):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))

    def __str__(self):
        """
        returns string version of square
        """
        string = ""
        if self.__size == 0:
            return string
        string += '\n' * self.__position[1]
        for i in range(self.__size):
            string += " " * self.__position[0]
            string += "#" * self.__size
            if i < self.__size - 1:
                string += "\n"
        return string
