#!/usr/bin/python3
if __name__ == "__main__":
    """Printing the sum of all the arguments."""
    import sys

    count = len(sys.argv)
    add = 0

    for i in range(1, count):
        add += int(sys.argv[i])
    print("{}".format(add))
