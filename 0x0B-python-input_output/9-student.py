#!/usr/bin/python3
"""Task 9 of ALX python input and output project

A class that defines a student (module)
"""


class Student:
    """A class that defines student"""

    def __init__(self, first_name, last_name, age):
        """initializing the attributes the class (student)"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieve dictionary definition of a student"""
        return self.__dict__
