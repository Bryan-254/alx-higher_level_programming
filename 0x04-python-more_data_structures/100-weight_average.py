#!/usr/bin/python3

def weight_average(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return 0

    # Calculate the weighted sum and total weight
    weighted_sum = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    # Return the weighted average
    if total_weight != 0:
        return weighted_sum / total_weight
    else:
        return 0
