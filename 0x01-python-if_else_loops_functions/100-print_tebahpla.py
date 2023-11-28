#!/usr/bin/python3
for x in range(122, 96, -1):
    # checks if the index is odd number
    if x % 2:
        # Difference btwn lowercase & uppercase letters is 32
        # Subtracting 32 from x converts it to the ASCII code
        # of the corresponding uppercase letter.
        x = x - 32
    print("{:c}".format(x), end="")
