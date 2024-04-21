#!/usr/bin/python3
""""Task 8 of ALX python input and output project

A function return dictionary description with simple
data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """Give a simple data structure for JSON serialization
    of object

    Argument:
        Obj (any type): at an instance of the class.

    Return:
        Dictionary representation the simple data structure.
    """
    return obj.__dict__
