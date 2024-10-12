#!/usr/bin/python3
"""print alphabet compose of alternate of upper
and lower cases in reverse order.
"""


for c in range(122, 96, -1):
    print("{}".format(chr(c) if (c % 2 == 0) else chr(c - 32)), end="")
