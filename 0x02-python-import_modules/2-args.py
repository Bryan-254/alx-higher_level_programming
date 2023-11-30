#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    x = 1

    if (len(sys.argv) == 1):
        print("0 arguments.")
    elif (len(sys.argv) == 2):
        print("{} argument:".format(x))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))

    if (len(sys.argv) != 1):
        for x in range(1, len(sys.argv)):
            print("{}: {}".format(x, sys.argv[x]))
