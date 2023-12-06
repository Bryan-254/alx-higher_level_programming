#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # Check if the key actually exists within the dictionary
    if key in a_dictionary:
        # If it exists, delete the key-value pair
        del a_dictionary[key]

    # Return modified dictionary
    return a_dictionary
