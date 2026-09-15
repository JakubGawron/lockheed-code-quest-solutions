import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re

for _ in range(int(input())):
    grid = [input() for _ in range(6)]
    letters = "ADFGVX"
    grid = {
        l + r: grid[y][x] for y, l in enumerate(letters) for x, r in enumerate(letters)
    }
    keyword = input()
    keyword_len = len(keyword)
    cipher = input()
    cipher = [cipher[i : i + keyword_len] for i in range(0, len(cipher), keyword_len)]
    left = "" if len(cipher[-1]) == keyword_len else cipher[-1]
    left_len = len(left)
    remaining = [""] * left_len
    if left:
        cipher = cipher[:-1]
        for i, char in enumerate(sorted(keyword[:left_len])):
            remaining[keyword.index(char)] = left[i]
    columns = dict(zip(sorted(keyword), map(list, zip(*cipher))))
    cipher = "".join(
        "".join(row) for row in zip(*[columns[char] for char in keyword])
    ) + "".join(remaining)
    print("".join(grid[cipher[i : i + 2]] for i in range(0, len(cipher), 2)))
