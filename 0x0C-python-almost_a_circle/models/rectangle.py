#!/usr/bin/python3
"""Task 2 - 9 & 13 of ALX unit test project

A module that defines a rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Representation of a rectangle class

    The rectangle is built on the base model class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle

        Args:
            width (int): The width of the new Rectangle
            height (int): The height of the new Rectangle
            x (int): The x coordinate of the new Rectangle
            y (int): The y coordinate of the new Rectangle
            id (int): The identity of the new Rectangle
        Raises:
            TypeError: If any of the values is not an int
            ValueError: If either of width or height <= 0
                        If either of x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Print the Rectangle in stdout using the `#` character"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle to assign an argument to each attribute

        Arguments:
            *args (ints): New attribute values
                - 1st argument rep id attribute
                - 2nd argument rep width attribute
                - 3rd argument rep height attribute
                - 4th argument rep x attribute
                - 5th argument rep y attribute
            **kwargs (dict): New key/value pairs of attributes
        """
        if args and len(args) != 0:
            idx = 0
            for mem in args:
                if idx == 0:
                    if mem is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = mem
                elif idx == 1:
                    self.width = mem
                elif idx == 2:
                    self.height = mem
                elif idx == 3:
                    self.x = mem
                elif idx == 4:
                    self.y = mem
                idx += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
