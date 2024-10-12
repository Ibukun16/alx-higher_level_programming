#!/usr/bin/python3
"""
Print numbers between 1 to 100 without
repition of digits
"""


for n in range(0, 10):
    for x in range(n + 1, 10):
        if n == 8 and x == 9:
            print("{}{}".format(n, x))
        else:
            print("{}{}".format(n, x), end=", ")
