#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has at least 2 elements, 
    # filling with 0 if needed
    a = tuple_a + (0, 0)[:max(0, 2 - len(tuple_a))]
    b = tuple_b + (0, 0)[:max(0, 2 - len(tuple_b))]

    # Sum the corresponding elements of the tuples
    new_tuple = (a[0] + b[0], a[1] + b[1])

    # Returns a tuple with 2 integers
    return new_tuple
