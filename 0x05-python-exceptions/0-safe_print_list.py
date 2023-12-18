#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        element_count = 0
        for y in range(x):
            print(my_list[y], end=" ")
            element_ count += 1
    except IndexError:
        pass
    finally:
        print()
        return element_count
