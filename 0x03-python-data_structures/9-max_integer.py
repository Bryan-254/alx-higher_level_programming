#!/usr/bin/python3

def max_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return None

    # Initialize the maximum value to the first element of the list
    maximum_value = my_list[0]

    # Iterate through the list to find the maximum value
    for number in my_list:
        if number > maximum_value:
            maximum_value = number

    return maximum_value
