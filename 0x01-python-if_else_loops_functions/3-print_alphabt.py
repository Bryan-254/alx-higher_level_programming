#!/usr/bin/python3
for x in range(97, 123):
    if (x == 101) or (x == 113):
        continue
    print(chr(x).format(), end="")
