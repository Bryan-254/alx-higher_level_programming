#!/usr/bin/python3

def best_score(a_dictionary):
    # Check to determine if dictionary is empty
    if not a_dictionary:
        # If empty, None is returned
        return None

    maximumValue_key = max(a_dictionary, key=a_dictionary.get)
    return maximumValue_key
