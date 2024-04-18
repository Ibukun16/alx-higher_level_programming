#!/usr/bin/python3
"""Task 8 of ALX project(python - inheritance)
A module that defines a child class that inherits
from a parent class."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """class that inherits from the BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new rectangle from BaseGeometry

        Arguments:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("heigt", height)
        self.__height = height
