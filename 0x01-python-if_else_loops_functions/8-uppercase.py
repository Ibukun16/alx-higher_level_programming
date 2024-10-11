#!/usr/bin/python3
def uppercase(str):
    output = ""
    for s in str:
        if 97 <= ord(s) <= 122:
            output += chr(ord(s) - 32)
        else:
            output += s
    print(output)
