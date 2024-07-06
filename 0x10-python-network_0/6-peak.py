#!/usr/bin/python3
"""A function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Get the peak in list of integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    bgn = 0
    size = len(list_of_integers)
    c = ((size - bgn) // 2) + bgn
    c = int(c)
    if size == 1:
        return list_of_integers[0]
    if size == 2:
        return max(list_of_integers)
    if list_of_integers[size - 1] >= list_of_integers[size - 2]:
        return list_of_integers[size - 1]
    for i in range(0, size - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and\
                list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]
