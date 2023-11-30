#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print(0)
    else:
        result = sum(int(arg) for arg in sys.argv[1:])
        print(result)
