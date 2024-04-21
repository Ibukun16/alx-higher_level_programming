#!/usr/bin/python3
"""Task 12 of ALX python input and output project

A function that returns a list of of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """A representation that defines the Pascal's triangle

    Return:
         A list of lists of integers representing the triangle
    """
    if n <= 0:
        return []
    res = [[1]]
    while len(res) != n:
        outLay = res[-1]
        inLay = [1]
        for i in range(len(outLay) - 1):
            inLay.append(outLay[i] + outLay[i + 1])
        inLay.append(1)
        res.append(inLay)
    return res
