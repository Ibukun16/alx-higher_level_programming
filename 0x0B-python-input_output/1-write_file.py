#!/usr/bin/python3
"""Task 1 of ALX python input/output project

A function that writes a string to a text file (UTF8) and return
the number of character written
"""


def write_file(filename="", text=""):
    """"Write a string to a text file and print
    the number of character

    Arguments:
        filename (str): path to the file to write

        text (str): The destination file receiving the text
    """
    with open(filename, "w", encoding="utf-8") as smyfile:
        smyfile.write(text)
        return len(text)
