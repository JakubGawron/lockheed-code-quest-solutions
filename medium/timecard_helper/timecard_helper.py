import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
def halfUpRound(value, q = 0, type = 'string'):
    rounded = Decimal(str(value)).quantize(Decimal('1').scaleb(-q), rounding=ROUND_HALF_UP)
    if type == 'string':
        return format(rounded, f'.{q}f')
    return float(rounded)

for _ in range(int(input())):
    T, E = map(int, input().split())
    ids = {}
    for _ in range(T):
        name, id = input().split(':')
        ids[name] = id

    tasks = defaultdict(int)
    for _ in range(E):
        name, time = input().split(':')
        tasks[ids[name]] += float(time)

    if sum(tasks.values()) <= 24:
        print('\n'.join(f'{k}:{halfUpRound(v, 1)}' for k, v in sorted(tasks.items())))
    else:
        print('Error')