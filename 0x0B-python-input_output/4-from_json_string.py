#!/usr/bin/python3
"""Task 4 of ALX python input/output project

A function that retursn an object (Python data structure)
represented by a JSON string.
"""


import json

def from_json_string(my_str):
    """return python data structure from JSON string

    Argument:
        my_str (str): The JSON file containing the string

    Return:
        The python data structure
    """
    return json.loads(my_str)
