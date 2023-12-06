#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Get the sorted keys
    ordered_keys = sorted(a_dictionary.keys())

    # Iterate through sorted keys and print key-value pairs
    for key in ordered_keys:
        value = a_dictionary[key]
        print(f"{key}: {value}")
