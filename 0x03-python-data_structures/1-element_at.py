#!/usr/bin/python3

def element_at(my_list, idx):
    # If it is negative
    if idx < 0:
        return None
    # If it is out of range
    elif idx >= len(my_list):
        return None
    # Return element at specified index
    return my_list[idx]
