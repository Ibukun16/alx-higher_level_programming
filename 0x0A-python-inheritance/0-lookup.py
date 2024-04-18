#!/usr/bin/python3
"""ALX Practise project task 0 (Python inheritance)

A module that defines object attribute lookup function.
"""


def lookup(obj):
    """Checkup object's available attributes

    Args:
        Obj: object.

    Return:
        list: Available methods and attributes of object.
    """
    return dir(obj)

