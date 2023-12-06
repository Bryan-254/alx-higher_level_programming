#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    # Create a copy of the dictionary 
    # This is to avoid modifying the original during iteration
    deletedKeysDict = [key for key, val in a_dictionary.items() if val == value]

    # Delete keys with the specified value
    for key in deletedKeysDict:
        del a_dictionary[key]
    return (a_dictionary)
