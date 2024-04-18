#!/usr/bin/python3
"""A Task in ALX Practise Project (Python Inheritance)

This Task contains a module that defines a function that
inherit from a parent class named Square
"""
Square = __import__("10-square").Square


class Square(Square):
    """Square class inherits from the Rectangle geometry"""

    def __init__(self, size):
        """Initialize a new square from geometry

        Arguments:
            size (int): The length of a side of the square
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Determine the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """"Description of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
