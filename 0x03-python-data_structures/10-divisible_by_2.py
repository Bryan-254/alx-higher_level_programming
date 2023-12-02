#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return []

    # Use list comprehension to create a new list of True or False
    new_list = [number % 2 == 0 for number in my_list]

    return new_list
