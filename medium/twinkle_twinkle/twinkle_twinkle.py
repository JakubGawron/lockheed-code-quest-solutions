import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
import math
#import string
#import re
from decimal import Decimal, ROUND_HALF_UP
def halfUpRound(value, q = 0, type = 'string'):
    rounded = Decimal(str(value)).quantize(Decimal('1').scaleb(-q), rounding=ROUND_HALF_UP)
    if rounded == Decimal('0'):
        rounded = abs(rounded)
    if type == 'string':
        return format(rounded, f'.{q}f')
    return float(rounded)

def getCords(r, a, x, y):
    return halfUpRound(r * math.cos(math.radians(a)) + x, 2) + ',' + halfUpRound(r * math.sin(math.radians(a)) + y, 2)

for _ in range(int(input())):
    x, y, p, r1, r2 = map(int, input().split())
    a, c = 90, 360 / p / 2
    points = []

    for i in range(p * 2):
        if i % 2:
            points.append(getCords(r2, a, x, y))
        else:
            points.append(getCords(r1, a, x, y))
        a += c

    print(' '.join(points))