#!/usr/bin/python3
"""
A module that defines a function which confirms an
object-class relationship
"""


def inherits_from(obj, a_class):
    """Check if a given object is an instance of
    a specified class directly or indirectly.

    Arguments:
        obj: The given object.
        a_class: The specified classs to find instance from.

    Return:
        bool: True, if the object is an instance of the class,
        and False for otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
