#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Get the peak in list of integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    top = len(list_of_integers)
    trough = 0
    midpnt = ((top - trough) // 2) + trough
    c = int(midpnt)
    if top == 1:
        return lists_of_integers[0]
    if top == 2:
        return max(list_of_integers)
    if list_of_integers[c] >= list_of_integers[c - 1] and\
            list_of_integers[c] >= list_of_integers[c + 1]:
        return list_of_integers[c]
    if c > 0 and list_of_integers[c] < list_of_integers[c + 1]:
        return find_peak(list_of_integers[c:])
    if c > 0 and list_of_integers[c] < list_of_integers[c - 1]:
        return find_peak(list_of_integers[:c])
