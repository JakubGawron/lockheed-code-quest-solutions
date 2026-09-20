import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re

from decimal import ROUND_HALF_UP, Decimal


def half_up_round(value, q=0, type="string"):
    rounded = Decimal(str(value)).quantize(
        Decimal(1).scaleb(-q), rounding=ROUND_HALF_UP
    )
    if rounded == Decimal(0):
        rounded = abs(rounded)
    if type == "string":
        return format(rounded, f".{q}f")
    return float(rounded)


ratio = {
    "Mercury": 0.377,
    "Venus": 0.905,
    "Earth": 1,
    "Mars": 0.379,
    "Jupiter": 2.528,
    "Saturn": 1.065,
    "Uranus": 0.886,
    "Neptune": 1.137,
}

for _ in range(int(input())):
    weight = int(input())
    for key, value in ratio.items():
        print(key + ":", half_up_round(value * weight, 1))
