#!/usr/bin/python3
"""
A class module that inherits
"""


class MyList(list):
    """
    class MyList that inherits from list
    """

    def print_sorted(self):
        """
        Function that sorts and prints the list
        """
        sorted_list = sorted(self)
        print(sorted_list)
