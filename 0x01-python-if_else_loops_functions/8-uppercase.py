#!/usr/bin/python3
"""Print upper case alphabet"""


def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()
