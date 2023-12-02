#!/usr/bin/python3
def no_c(my_string):
    modified_string = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            modified_string += elements
    return modified_string
