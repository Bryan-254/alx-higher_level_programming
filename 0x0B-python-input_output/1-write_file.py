#!/usr/bin/python3
"""
Write to a file task
"""


def write_file(filename="", text=""):
    """
    The with open statement is a convenient way to open a
    file and automatically close it when the block of code
    inside the with statement is exited.

    function directly returns the result of file.write(text),
    which is the number of characters written.

    This code writes the specified text to the file using file.write(text)
    and then returns the number of characters written directly without the
    need for an intermediate variable.
    """

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
