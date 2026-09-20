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


G = 6.673e-11
M = 5.98e24
Re = 6.37e6

for _ in range(int(input())):
    height = int(input())

    radius = Re + height

    velocity = math.sqrt((G * M) / radius)
    period = int(half_up_round(math.sqrt((4 * math.pi**2 * radius**3) / (G * M))))

    velocity = half_up_round(velocity)

    hours = period // 3600
    minutes = (period % 3600) // 60
    seconds = period % 60

    formatted_time = f"{hours}:{minutes:02d}:{seconds:02d}"

    print(velocity, formatted_time)
