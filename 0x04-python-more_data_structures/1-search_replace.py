#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """A function that searches for and replace an element
    in a new list"""
    return [replace if i == search else i for i in my_list]
