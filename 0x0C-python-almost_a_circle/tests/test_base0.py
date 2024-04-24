#!/usr/bin/python3
"""Task 0 of ALX python unittests

The base class for unittests

Unittest Classes:
    Basetest_calculations -
"""

import unittest
from my_calculations import calculations


class Basetest_calculations(unittest.TestCase):
    """unittest for tetsing calculations base class."""

    def setUp(self):
        self.calculate = calculations(12, 3)

    def test_sum(self):
        self.assertEqual(self.calculate.get_sum(), 15,
                'The sum is wrong.')

    def test_diff(self):
        self.assertEqual(self.calculate.get_diff(), 9,
                'The difference is wrong.')

    def test_prod(self):
        self.assertEqual(self.calculate.get_prod(), 36,
                'The result is wrong.')

    def test_quotient(self):
        self.assertEqual(self.calculate.get_quotient(), 4,
                'The result is wrong.')

