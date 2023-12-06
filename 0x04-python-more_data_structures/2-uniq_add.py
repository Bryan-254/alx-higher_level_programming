#!/usr/bin/python3

def uniq_add(my_list=[]):
    # set is used to keep track of unique integers encountered in the list
    unique_list = set(my_list)
    return sum(unique_list)
