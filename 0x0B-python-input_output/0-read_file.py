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

    content = file.read(): This line reads the entire content of
    the file using the read() method and stores it in the variable 'content'.

    print(content): This line prints the content of the file
    to the standard output (stdout). 
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"Error reading file: {e}")
