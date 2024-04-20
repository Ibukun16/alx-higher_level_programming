#!/usr/bin/python3
"""Task 0 of ALX Python Input/Output file Project

A function that read a text file (UTF-8) and print to stdout.
"""


def read_file(filename=""):
    """read a file name and print its content to stdout
    
    argument:
        filename (str): The path to the file.
    """

    with open(filename, "r", encoding="utf-8") as myfile:
        print(myfile.read(), end="")
