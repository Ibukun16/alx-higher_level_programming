#!/usr/bin/python3
"""Task 5 of ALX python input and output project

A function that writes an Object to a text file using
JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file using JSON
    representation.

    Arguments:
        my_obj (any type): The object file to write from

        filename (str): The text file receiving the wriiten object
    """
    with open(filename, "w", encoding="utf-8") as newFile:
        json.dump(my_obj, newFile)
