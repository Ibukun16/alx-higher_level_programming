#!/usr/bin/python3
"""ALX Practise project task 0 (Python inheritance)

A module that defines object attribute lookup function.
"""


def lookup(obj):
    """Checkup object available function and return a
    list of the available methods and attributes found.
    """
    return dir(obj)

