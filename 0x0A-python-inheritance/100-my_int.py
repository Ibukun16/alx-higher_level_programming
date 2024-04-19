#!/usr/bin/python3
""""Advance task of ALX Python inheritance project
This module defines a class that inherits the ``int`` class
"""


class MyInt(int):
    """Invert operators == and !=."""

    def __eq__(self, value):
        """eq"""
        return self.real != value

    def __ne__(self, value):
        """ne"""
        return self.real == value
