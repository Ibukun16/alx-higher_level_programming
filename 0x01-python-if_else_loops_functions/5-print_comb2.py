#!/usr/bin/python3
"""Print number from 0 to 99"""


for n in range(0, 100):
    print("{}".format(n:02), end=", " if n < 99 else "\n")
