#!/usr/bin/python3
"""
Append to a file task
"""


def append_write(filename="", text=""):
    """
    'a' is used as the mode parameter to open the file in append mode,
    and "utf-8" specifies the encoding of the file.

    The with statement is used to ensure that the file is properly closed
    after the operations inside the block are executed.

    The write method of the file object is used to append
    the specified text to the file.

    The function returns then number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
