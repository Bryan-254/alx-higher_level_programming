#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]

    numof_args = len(argv)

    if numof_args == 0:
        print("0 arguments.")
    elif numof_args == 1:
        print("1 argument:")
        print(f"1: {argv[0]}")
    else:
        print(f"{numof_args} arguments:")
        for x, arg in enumerate(argv, start=1):
            print(f"{x}: {arg}")
