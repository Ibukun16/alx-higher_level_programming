#!/usr/bin/python3
def element_at(my_list, idx):
    """Print the element index by a given value"""
    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
