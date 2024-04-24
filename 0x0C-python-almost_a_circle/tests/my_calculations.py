#!/usr/bin/python3
"""Task 0 apply unit testing example

my_calculations test examples
"""


class calculations:
    """perform simple arithmetic calculations"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_sum(self):
        """Find the sum of 2 numbers"""
        return self.x + self.y

    def get_diff(self):
        """Find the difference of 2 numbers"""
        return self.x - self.y

    def get_prod(self):
        """Find the product of 2 numbers"""
        return self.x * self.y

    def get_quotient(self):
        """Find the quotient of a number by another number"""
        return self.x / self.y

