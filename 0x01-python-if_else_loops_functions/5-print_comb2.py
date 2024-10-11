#!/usr/bin/python3
for n in range(100):
    print(f"{n:02}", end=", " if n < 99 else "\n")
