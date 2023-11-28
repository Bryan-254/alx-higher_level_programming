#!/usr/bin/python3
for x in range(97, 123):
    if (x == 'e') or (x == 'q'):
        continue
    print(chr(x).format(), end="")
