#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    # The lambda function multiplies each element by the given number.
    # Map is used where you want to apply a function 
    # to multiple iterables simultaneously.
    return list(map(lambda y: y * number, my_list))
