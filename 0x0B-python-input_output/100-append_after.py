#!/usr/bin/python3
"""Task 13 of ALX python input and output project

A function that insert a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text to a file, after each line containing
    specific string.

    Arguments:
        filename (str): The file having the text to be worked on

        search_string (str): The referenced string to search for in the text

        new_string (str): The string to be inserted
    """

    with open(filename, "r+", encoding="utf-8") as theFile:
        txt = ""
        for line in theFile:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w", encoding="utf-8") as toFile:
        toFile.write(txt)
