#!/usr/bin/python3
"""
Search and update task
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Open the file in read mode to retrieve its content.

    Open the file in write mode to overwrite its content.
    Iterate through each line in the original content.
    Write the original line to the file.
    Check if the search string is present in the line.
    If found, append the new string after the line.
    """

    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
