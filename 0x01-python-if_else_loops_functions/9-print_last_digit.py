#!/usr/bin/python3
def print_last_digit(number):
    # Ensure number is positive
    number = abs(number)

    # Get the last digit
    last_dig = number % 10

    # Print the last digit
    print("{:d}".format(last_dig), end="")

    # Return the last digit value
    return (last_dig)
