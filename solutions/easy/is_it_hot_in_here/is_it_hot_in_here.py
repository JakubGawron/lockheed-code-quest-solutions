import sys

input = lambda: sys.stdin.readline().rstrip()

# import string
# import re

for _ in range(int(input())):
    for _ in range(int(input())):
        line = input()
        temp, scale = line.split()
        temp = float(temp)

        if scale == "F":
            temp = (5 / 9) * (temp - 32)
            scale = "C"
        else:
            temp = (9 / 5 * temp) + 32
            scale = "F"

        print(f"{line} = {temp:.1f} {scale}")
