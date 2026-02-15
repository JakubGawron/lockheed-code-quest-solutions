import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
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

def getNumericValueOfDataBlock(data):
    return sum([string.ascii_lowercase.index(char) + 1 for char in data])

def getBlockHash(n, H, V, T):
    return (T + V + n + H) * 50 / 147

for _ in range(int(input())):
    H = 0
    V = [getNumericValueOfDataBlock(input) for input in input().split()]
    T = list(map(int, input().split()))

    for n in range(10):
        H = getBlockHash(n + 1, H, V[n], T[n])
    print(halfUpRound(H, 0))