#!/usr/bin/python3
"""Task 11 of ALX python input and output project

A class function that defines a student class based on Task 10
"""



class Student:
    """A representation that defines a student class"""

    def __init__(self, first_name, last_name, age):
        """Initialization of the student class definition"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a student instance

        If attrs is a list strings, only attributes name contain in the
        list must be retrieved, else retrieve all attributes

        Arguments:
            attrs (list): (Optional) The attributes to be represented
        """
        if (type(attrs) is list and all(type(mem) == str for mem in attrs)):
            return {mem: getattr(self, mem) for mem in attrs if hasattr(self, mem)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the student instances

        Arguments:
            json (dict): The attributes: values to replace the attributes
        """
        for key, value in json.items():
            setattr(self, key, value)
