#!/usr/bin/python3
"""
function that prints a square with the character #
"""


def print_square(size):
    """
    If size is not an instance of int class, raise TypeError
    If size is less than zero, Raise ValueError
    If size is an instance of float and less than zero, raise TypeError
    Print a square made of # characters.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
