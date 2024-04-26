#!/usr/bin/python3
"""Task 14 of the ALX python input/output project

A script that reads stdin line by line and compute metrics

Conditions:
    After every 10 lines and after a keyboard interruption
    (CTRL + C), print the statistics since the beginning

    - Print total file size up to that point
    - Print status code up to that point in asceding order.
"""


def print_stats(size, status_code):
    """Print the accumalated values.

    Arguments:
        size (int): The size of the accumulated read file.
        status_codes (dict): The count of the status code.
    """
    print("File size: {}".format(size))
    for key in sorted(status_code):
        print("{}: {}". format(key, status_code[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_code = {}
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    c = 0

    try:
        for line in sys.stdin:
            if c == 10:
                print_stats(size, status_code)
                c = 1
            else:
                c += 1
            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in codes:
                    if status_code.get(line[-2], -1) == -1:
                        status_code[line[-2]] = 1
                    else:
                        status_code[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_code)

    except KeyboardInterrupt:
        print_stats(size, status_code)
        raise
