#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """A function that return a new dictionary with
    each value multiplied by 2"""
    return ({key: a_dictionary[key] * 2 for key in a_dictionary})
