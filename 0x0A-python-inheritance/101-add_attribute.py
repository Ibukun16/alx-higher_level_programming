#!/usr/bin/python3
"""Task 13 of the ALX Python inheritance project.

A module that defines a function that add attributes to objects
"""


def add_attribute(obj, attr, value):
    """Add an attribute to an object where possible

    Arguments:
        obj (any): The object to add an attribute
        attr (str): The attribute to add to the object
        value (any): The value of the attribute to add.

    Raises:
        TypeError: when no attribute can be added to the obj
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
