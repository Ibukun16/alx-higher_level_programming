#!/usr/bin/python3
"""
A module that defines a function that confirms an
 object-class relationship
"""


def is_same_class(obj, a_class):
    """Check if the object is an instance of the
     specified class.

    Args:
        obj: Object to be checked
        a_class: The class to find from.

    Return:
        bool: True, if the it is an instance, and false for otherwise.
    """
    return type(obj) is a_class
