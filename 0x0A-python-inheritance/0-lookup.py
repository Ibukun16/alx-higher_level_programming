#!/usr/bin/python3
"""ALX Practise project task 0 (Python inheritance)

A module that defines object attribute lookup function.
"""


def lookup(obj):
    """Checkup available functions and methods for an object


    Arguments:
        obj: The object to find its attributes

    Return:
        list: Available methods and attributes found.
    """
    return dir(obj)
