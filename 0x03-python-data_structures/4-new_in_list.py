#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Create a copy of og list
    new_list = my_list[:]

    # If negative, return a copy of the og list
    if idx < 0:
        return new_list

    # If out of range, return a copy of the og list
    if idx >= len(my_list):
        return new_list

    # Replace the element at specified index in the new_list with the new value
    new_list[idx] = element

    return new_list
