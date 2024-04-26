#!/usr/bin/python3
"""Task 10 of ALX python input and output project

A class that defines student based on Task 9
"""


class Student:
    """A representation of the class, student"""

    def __init__(self, first_name, last_name, age):
        """Initializing the defination of the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """"Retrieves a dictionary representation of a student instance

        If attrs is a lists of strings, represent only those attributes
        included in those lists.

        Arguments:
            attrs (lists): The attributes to be represented (optional)
        """
        if (type(attrs) is list and all(type(mem) is str for mem in attrs)):
            return {mem: getattr(self, mem) for mem in attrs if hasattr(self, mem)}
        return self.__dict__
