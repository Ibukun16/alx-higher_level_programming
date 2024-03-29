#!/usr/bin/python3
if __name__ == "__main__":
    """Do basic maths operations with imported functions."""
    from calculator_1 import add, sub, mul, div
    import sys

    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    op = sys.argv[2]
    if op not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, op, b, ops[op](a, b)))
