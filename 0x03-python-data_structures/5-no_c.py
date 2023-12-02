#!/usr/bin/python3
def no_c(my_string):
    # Initialized as an empty string ("") before the loop
    modified_string = ""

    for elements in my_string:
        if elements != "c" and elements != "C":
            # concatenating the current element to the modified string
            modified_string += elements
    # String w/out c and C is returned
    return modified_string
