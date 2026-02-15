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
    a, op, b = input().split()
    a = int(a)
    b = int(b)
    res = 0
    if op == '+':
        res = [a+b]*2
    elif op == '-':
        res = [a-b, b-a]
    elif op == '*':
        res = [a*b]*2
    else:
        res = [a/b, b/a]
    print(' '.join([halfUpRound(num, 1) for num in res]))