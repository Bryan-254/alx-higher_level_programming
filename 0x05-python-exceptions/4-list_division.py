#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Function that divides two lists element by element.

    Args:
        my_list_1 (list): This is the  first list.
        my_list_2 (list): This is the  second list.
        list_length (int): The length list/number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    fresh_list = []
    for i in range(0, list_length):
        try:
            divresult = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            divresult = 0
        except ZeroDivisionError:
            print("division by 0")
            divresult = 0
        except IndexError:
            print("out of range")
            divresult = 0
        finally:
            fresh_list.append(divresult)
    return (fresh_list)
