import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re

types = [["SECONDS", 1], ["MINUTES", 60], ["HOURS", 60], ["DAYS", 24]]
for _ in range(int(input())):
    v, from_v, to_v = input().split()
    v = int(v)
    i_from = next(i for i, type in enumerate(types) if type[0] == from_v)
    i_to = next(i for i, type in enumerate(types) if type[0] == to_v)

    d = 1 if i_to - i_from >= 0 else -1
    converted = v
    if d < 0:
        while i_from != i_to:
            converted *= types[i_from][1]
            i_from += d
    else:
        while i_from != i_to:
            i_from += d
            converted /= types[i_from][1]
    print(f"{v} {from_v}->{int(converted)} {to_v}")
