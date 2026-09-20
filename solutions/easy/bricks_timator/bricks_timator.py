import sys

input = lambda: sys.stdin.readline().rstrip()
import math

# import string
# import re

for _ in range(int(input())):
    dimensions, height, _, integers = input().split(maxsplit=3)
    L, H = map(int, dimensions.split("x"))
    height = int(height)
    width = sum(map(int, integers.split()))
    print(math.ceil((height * width) / (L * H)))
