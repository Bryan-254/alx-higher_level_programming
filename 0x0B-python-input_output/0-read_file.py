#!/usr/bin/python3
"""
Read file task
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout.

    The encoding='utf-8' argument ensures that the file is read
    using UTF-8 encoding.

    The with open statement is a convenient way to open a
    file and automatically close it when the block of code
    inside the with statement is exited.

    The line, print(file.read(), end=""), is responsible for reading
    the content of the file opened with the with open statement and
    printing it to the standard output.

    The end="" parameter ensures that there is no newline character (\n)
    added at the end of the printed content.
    """

    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
