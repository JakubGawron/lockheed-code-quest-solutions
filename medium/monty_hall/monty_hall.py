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

def getCurrentChance(sum_chance, left_doors):
    chance = (100 - sum_chance) / left_doors
    return (chance, sum_chance + chance)

for _ in range(int(input())):
    left_doors, rounds, openedAtOnce = map(int, input().split())
    chance = getCurrentChance(0, left_doors)

    for _ in range(rounds):
        left_doors -= openedAtOnce + 1
        chance = getCurrentChance(chance[1], left_doors)

    print(halfUpRound(chance[0], 2) + '%')