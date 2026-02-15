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

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

for _ in range(int(input())):
    dividend, divisor = input().split()
    if not is_number(dividend):
        print('Invalid Dividend')
    elif not is_number(divisor):
        print('Invalid Divisor')
    else:
        dividend, divisor = map(float, (dividend, divisor))
        if divisor == 0:
            print('Divide By Zero')
        else:
            print(halfUpRound(dividend / divisor, 1))