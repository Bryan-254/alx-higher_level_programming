#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # One could use ^ operator.
    # When used between two sets, it returns a new set containing
    # elements that are unique to each set
    # return set_1 ^ set_2
    # Or we could calculate the symmetric difference between set_1 and set_2
    onlyOneSet_elements = set_1.symmetric_difference(set_2)
    return onlyOneSet_elements
