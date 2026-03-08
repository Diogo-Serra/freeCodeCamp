#!/usr/bin/env python3

def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    return " ".join(str(i) for i in range(1, n + 1))


strout = number_pattern(5)
print(strout)
