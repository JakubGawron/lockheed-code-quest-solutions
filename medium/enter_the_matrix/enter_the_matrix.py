import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
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

for _ in range(int(input())):
    a, b = map(float, input().split())
    c, d = map(float, input().split())
    F1, F2 = map(float, input().split())

    rev_C = [num/(a*d-b*c) for num in [d, -b, -c, a]]
    E = [halfUpRound((num1 * F1) + (num2 * F2), 1)[:-2] for num1, num2 in [rev_C[::2], rev_C[1::2]]]
    print(' '.join(E))