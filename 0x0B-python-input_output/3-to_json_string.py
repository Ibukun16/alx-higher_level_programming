#!/usr/bin/python3
"""Task 3 of ALX python input/output project

A function that prints JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """Return the json representation of the string

    Argument:
        my_obj (any type): The object to be represented

    Return:
        The json file
    """
    return json.dumps(my_obj)
