#!/usr/bin/python3
"""
A module that defines a function which confirms an
object class relationship
"""

def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of a class
    or an instance ofthe class inheritance.

    Arguments:
        obj: The object to be checked
        a_class: The class to find the instance from

    Return:
        bool: True, if it is an instance, and False if not.
    """
    return isinstance(obj, a_class)
