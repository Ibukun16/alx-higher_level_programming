#!/usr/bin/python3
"""Print alphabet excluding letter e and q"""
for alphabet in range(97, 123):
    if chr(alphabet) != 'q' and chr(alphabet) != 'e':
        print(f"{chr(alphabet)}", end="")
