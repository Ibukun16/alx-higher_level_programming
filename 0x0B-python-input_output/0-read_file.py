#!/usr/bin/python3
"""Task 0 of ALX Python Input/Output file Project

A function that read a text file (UTF8) and output the result
"""


def read_file(filename=""):
    """read a file name and print its content to stdout

    argument:
        filename (str): The path to the file.
    """

    with open(filename, "r", encoding="utf-8") as newfile:
        print(newfile.read(), end="")
