#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    newList = []

    # Iterate through the elements in the original list
    for elmt in my_list:
        # Check if the current element is equal to the search element
        if elmt == search:
            # If yes, replace it with the new element
            newList.append(replace)
        else:
            # If not, keep the original element
            newList.append(elmt)

    return newList
