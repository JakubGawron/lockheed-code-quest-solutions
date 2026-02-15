import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

from decimal import Decimal, ROUND_HALF_UP
def halfUpRound(value, q = 0, type = 'string'):
    rounded = Decimal(str(value)).quantize(Decimal('1').scaleb(-q), rounding=ROUND_HALF_UP)
    if type == 'string':
        return format(rounded, f'.{q}f')
    return float(rounded)

for _ in range(int(input())):
    M, S = map(int, input().split())

    materials = {}
    for _ in range(M):
        mat, rad = input().split()
        materials[mat] = float(rad)

    for _ in range(S):
        mat, thic, absortion = input().split()
        rad_per_sec = float(absortion) - (materials[mat] * float(thic))
        if rad_per_sec > 0:
            print(halfUpRound(50 / rad_per_sec, 2))
        else:
            print('Infinity')