#!/usr/bin/python3
"""Task 9 of ALX project (Python inheritance)
A module that defines a child class as preceding task
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """child class that inherit from the base class"""

    def __init__(self, width, height):
        """Initialize a new rectangle from the BaseGeometry

        Arguments:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """"Define the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """Return the string representing the result of rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
