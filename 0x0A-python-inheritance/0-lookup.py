#!/usr/bin/python3
"""
ALX Practise project task 0
A module that defines an object
attribute lookup function.
"""


def lookup(obj):
    """
    Checkup object's available attributes

    Args: Obj - object.

    Return type: List - Available methods and
    attributes of an object.
    """
    return dir(obj)

