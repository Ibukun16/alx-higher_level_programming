#!/usr/bin/python3
def uniq_add(my_list=[]):
    """A function that add up unique integers in a list"""
    sum = 0

    for x in list(set(my_list)):
        sum += x
    return sum
