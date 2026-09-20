import sys

input = lambda: sys.stdin.readline().rstrip()
import math

# import string
# import re

for _ in range(int(input())):
    total_area = int(input())
    areas = []
    while total_area:
        max = math.floor(math.sqrt(total_area))
        area = max**2
        areas.append(area)
        total_area -= area
    print(areas)
