#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    # If negative, return og list
    if idx < 0:
        return my_list

    # If out of range, return og list
    if idx >= len(my_list):
        return my_list

    # Replace the element at specified index in the list with the new value
    my_list[idx] = element

    # returns the modified list
    return my_list
