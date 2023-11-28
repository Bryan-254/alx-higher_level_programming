#!/usr/bin/python3

for x in range(9):
    for y in range(x + 1, 10):
        if x * 10 + y < 89:
            print("{:d}{:d}".format(x, y), end=", ")
print("{:d}".format(89))
