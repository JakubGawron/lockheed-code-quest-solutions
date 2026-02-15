import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
import string
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
    total = 0
    occurances = {}
    for letter in string.ascii_uppercase:
        occurances[letter] = 0
    for _ in range(int(input())):
        text = input().upper()
        for letter in text:
            if 'A' <= letter <= 'Z':
                total += 1
                occurances[letter] += 1
    
    for letter, occurence in sorted(occurances.items(), key=lambda k: k[0]):
        print(f'{letter}: {halfUpRound(occurence/total*100, 2)}%')