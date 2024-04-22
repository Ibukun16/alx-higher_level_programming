#!/usr/bin/python3
"""Task 6 of ALX Python input and output project

A function that creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """Create an Object from a JSON file

    Arguments:
        filename: The file to create the object from
    """
    with open(filename, "r", encoding="utf-8") as objfile:
        objname = objfile.read()
        return json.loads(objname)
