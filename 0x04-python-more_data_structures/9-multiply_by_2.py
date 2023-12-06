#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the multiplied values
    multipliedValues_dictionary = {}

    # Iterate through the items in the input dictionary
    for key, value in a_dictionary.items():
        # Multiply each value by 2 and store it in new dictionary
        multipliedValues_dictionary[key] = value * 2

    # Return new dictionary containing multiplied values
    return multipliedValues_dictionary
