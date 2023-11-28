#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord("A") <= ord(x) <= ord("Z"):
            x = chr(ord(x) - 32)
        print("{:s}".format(x), end="")
    print()
