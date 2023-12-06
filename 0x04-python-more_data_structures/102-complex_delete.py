#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys = []

    for key, val in a_dictionary.items():
        if val is value:
            keys.append(key)

    for y in range(len(keys)):
        # Delete keys with the specified value
        del a_dictionary[keys[y]]

    # Return the dictionary
    return (a_dictionary)
