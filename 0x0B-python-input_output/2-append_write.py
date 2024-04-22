#!/usr/bin/python3
"""Task 2 of ALX python input/output project

A function that appends a string at the end of a text file (UTF8)
and return the number of characters added
"""


def append_write(filename="", text=""):
    """Add a string to the end of a text and print number of characters

    Arguments:
        filename (str): The path to the file to append

        text (str): The destination file receiving the text
    """
    with open(filename, "a", encoding="utf-8") as Tmyfile:
        Tmyfile.write(text)
        return len(text)
