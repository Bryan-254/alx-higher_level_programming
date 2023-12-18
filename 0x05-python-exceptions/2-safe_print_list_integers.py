#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elementcount = 0

    try:
        for y in range(x):
            if isinstance(my_list[y], int):
                print("{:d}".format(my_list[y]), end="")
                elementcount += 1
    except IndexError:
        pass
    finally:
        print()
        return elementcount
