#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Get the peak in list of integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    span = len(list_of_integers)
    zero = 0
    midpnt = ((span - zero) // 2) + zero
    c = int(midpnt)
    if span == 1:
        return lists_of_integers[0]
    if span == 2:
        return max(list_of_integers)
    if list_of_integers[c] >= list_of_integers[c - 1] and\
            list_of_integers[c] >= list_of_integers[c + 1]:
        return list_of_integers[c]
    if c > 0 and list_of_integers[c] < list_of_integers[c + 1]:
        return find_peak(list_of_integers[c:])
    if c > 0 and list_of_integers[c] < list_of_integers[c - 1]:
        return find_peak(list_of_integers[:c])
