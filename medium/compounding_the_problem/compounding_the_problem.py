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
    D = int(input())
    A = 0
    ending_balance = 0
    for _ in range(D):
        day, pucharses, payments = input().split(',')
        ending_balance += (0 if pucharses == '' else float(pucharses)) - (0 if payments == '' else float(payments))
        A += ending_balance
        
    
    print('$' + halfUpRound((A/D)*0.015, 2))