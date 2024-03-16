#!/usr/bin/python3

if __name__ == "__main__":
    """A programme that prints the number and list of its argument"""
    import sys

    count = len(sys.argv) - 1

    if count <= 1:
        argument = "argument"
    else:
        argument = "arguments"

    if count == 0:
        print("{} {}.".format(count, argument))
    else:
        print("{} {}:".format(count, argument))

    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
