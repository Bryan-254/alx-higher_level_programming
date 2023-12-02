#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # If negative, return og list
    if idx < 0:
        return my_list

    # If out of range, return og list
    elif idx >= len(my_list):
        return my_list

    # Delete an element at a specified position in a list
    del my_list[idx]

    # Returns the modified list
    return my_list
