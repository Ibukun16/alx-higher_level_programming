#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace and element of a list at a given index"""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
        return my_list
    else:
        return my_list
