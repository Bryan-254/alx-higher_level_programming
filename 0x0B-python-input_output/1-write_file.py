#!/usr/bin/python3
"""
Write to a file task
"""


def write_file(filename="", text=""):
    """
    The with open statement is a convenient way to open a
    file and automatically close it when the block of code
    inside the with statement is exited.

    This code writes the specified text to the file using file.write(text)
    and then prints the number of characters written directly without the
    need for an intermediate variable.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        print(file.write(text), end="")
