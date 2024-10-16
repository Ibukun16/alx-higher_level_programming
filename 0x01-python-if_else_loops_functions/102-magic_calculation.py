#!/usr/bin/python3
"""Perform operations similar to bytecode"""


def magic_calculation(a, b, c):
    """Match bytecode"""
    if a < b:
        return c
    if c > b:
        return a + b
    return a*b - c
