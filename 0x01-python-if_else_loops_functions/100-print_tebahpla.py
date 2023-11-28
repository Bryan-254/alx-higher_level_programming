#!/usr/bin/python3
for x in range(ord('z'), ord('A') - 1, -1):
    print("{}".format(chr(x) if x % 2 == 1 else chr(x).upper()), end='')
