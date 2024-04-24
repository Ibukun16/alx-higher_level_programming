#!/usr/bin/python3
"""Task 10 - 19 of ALX unit test project

A module that defines a square class""" 
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of a square class

    A square class is built on the rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square

        Args:
            size (int): The length of a side of the new Square
            x (int): The x coordinate of the new Square
            y (int): The y coordinate of the new Square
            id (int): The identity of the new Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Add the public setter and getter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square to assign an argument to each attribute 
        by public method

        Args:
            *args (ints): New attribute values
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes
        """
        if args and len(args) != 0:
            idx = 0
            for mem in args:
                if idx == 0:
                    if mem is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = mem
                elif idx == 1:
                    self.size = mem
                elif idx == 2:
                    self.x = mem
                elif idx == 3:
                    self.y = mem
                idx += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of the Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
