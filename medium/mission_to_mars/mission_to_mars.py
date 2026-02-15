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
    distance, speed = map(float, input().split())
    hours = distance * 10 ** 6 / speed
    days, hours = divmod(hours, 24)
    hours, minutes = divmod(hours * 60, 60)
    minutes, seconds = divmod(halfUpRound(minutes * 60, 0, 'float'), 60)
    print(f'Time to Mars: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds')