#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find and print the biggest among a set of integers"""
    if my_list == []:
        return None
    else:
        max_list = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max_list:
            max_list = my_list[i]
    return max_list
