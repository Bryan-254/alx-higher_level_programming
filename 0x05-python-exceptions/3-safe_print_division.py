#!/usr/bin/python3

def safe_print_division(a, b):
    """Function returns the division of a by b."""
    try:
        divresult = a / b
    except (TypeError, ZeroDivisionError):
        divresult = None
    finally:
        print("Inside result: {}".format(divresult))
    return (divresult)
