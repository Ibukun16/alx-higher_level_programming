#!/usr/bin/python3
"""
A module that defines a function that return an empty class
and raises an exception.
"""


class BaseGeometry:
    """Do nothing and return an empty class with
    an exception clause."""

    def area(self):
        """Raise an Error"""
        raise Exception("area() is not implemented")
