#!/usr/bin/python3
"""
A module that defines a class that inherit from List
"""

class MyList(list):
    """"
    Inherit sorted printing from the built-in list class
    """
    def print_sorted(self):
        """Print list sorted in ascending order"""
        print(sorted(self))
