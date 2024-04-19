#!/usr/bin/python3
"""
A module that defines class which does random task
"""


class BaseGeometry:
    """Defining the representation of the base geometry"""

    def area(self):
        """Return an Error message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Determine if a value is an integer

        Arguments:
            name (str): Name of the object.
            value (int): The value to validate.

        Raises:
            TypeError: If value type is not an integer.
            ValueError: If value is less than or equals 0.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))
