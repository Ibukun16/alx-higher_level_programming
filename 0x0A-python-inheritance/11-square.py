#!/usr/bin/python3
"""A Task in ALX Practise Project (Python Inheritance)

This Task contains a module that defines a function that
inherit from a parent class named Square
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class inherits from the Rectangle geometry"""

    def __init__(self, size):
        """Initialize a new square based on a rectangle geometry

        Arguments:
            size (int): The length of a side of the square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Define the area of a square"""
        return self.__size * self.__size

    def __str__(self):
        """"Description of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
