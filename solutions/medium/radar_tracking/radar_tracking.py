import sys

input = lambda: sys.stdin.readline().rstrip()
import math

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


def get_cordinates(angle, r):
    angle = math.radians(angle)
    return r * math.cos(angle), r * math.sin(angle)


for _ in range(int(input())):
    angle_before, distance_before, angle_after, distance_after = map(
        int, input().split()
    )
    x1, y1 = get_cordinates(angle_before, distance_before)
    x2, y2 = get_cordinates(angle_after, distance_after)
    dx, dy = x2 - x1, y2 - y1

    speed = half_up_round(math.sqrt(dx**2 + dy**2) * 10)
    heading = half_up_round(math.degrees(math.atan2(dy, dx)) % 360)
    print(speed, heading)
