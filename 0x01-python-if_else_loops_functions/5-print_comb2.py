#!/usr/bin/python3
"""Print number from 0 to 99"""


for n in range(0, 100):
    if n == 99:
        print("{}".format(n))
    else:
        print("{:02}".format(n), end=", ")
