import sys
input = lambda: sys.stdin.readline().rstrip()
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
    n = int(input())
    ev = sum(map(float, input().split()))
    ac = sum(map(float, input().split()))
    print(halfUpRound((ac-ev)/n, 2))