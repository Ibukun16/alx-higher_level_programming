#!/usr/bin/python3
"""
ALX Practise project task 0

A module that defines object attribute lookup function.
"""


def lookup(obj):
    """
    Checkup object's available attributes

    Args: Obj - object.

    Return: List of available methods and attributes of an object.
    """
    return dir(obj)

