#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord("a") <= ord(x) <= ord("z"):
            x = chr(ord(x) - 32)
        print("{:s}".format(x), end="")
    print()
