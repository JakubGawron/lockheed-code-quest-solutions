import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    name, stats = input().split(':')
    stats = stats.split(',')
    stats = [stat for stat in stats if stat != 'BB']
    totalAtBats = len(stats)

    if totalAtBats: 
        slg = (stats.count('1B') + (2*stats.count('2B')) + (3*stats.count('3B')) + (4*stats.count('HR')))/totalAtBats
    else:
        slg = 0
    print(f'{name}={round(slg, 3):.3f}')