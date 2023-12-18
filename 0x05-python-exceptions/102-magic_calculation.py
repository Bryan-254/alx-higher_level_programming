#!/usr/bin/python3
def magic_calculation(a, b):
    accumulatedresult = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            accumulatedresult += a ** b / i
        except Exception:
            accumulatedresult = b + a
            break
    return accumulatedresult
