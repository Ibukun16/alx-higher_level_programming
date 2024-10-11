#!/usr/bin/python3
for n in range(10):
    for x in range(n + 1, 10):
        print(f"{n}{x}", end=", " if n < 8 or (n == 8 and x < 9) else "\n")
