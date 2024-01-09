#!/usr/bin/python3
"""
Search and update task
"""


def append_after(filename="", search_string="", new_string=""):
    """
    append_after function seems to be designed to open a file,
    search for a specific string (search_string), and then append
    a new string (new_string) after each occurrence of the search string.
    """

    txt = ""
    with open(filename) as r:
        for line in r:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
