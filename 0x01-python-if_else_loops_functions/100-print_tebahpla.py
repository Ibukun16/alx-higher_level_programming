#!/usr/bin/python3
"""print alphabet compose of alternate of upper
and lower cases in reverse order.
"""


print("".join(chr(122 - c) if c % 2 == 0 else chr(90 - c)
      for c in range(26)), end="")
