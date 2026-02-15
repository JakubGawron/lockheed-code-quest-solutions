import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
import math
#import string
#import re

for _ in range(int(input())):
    sum = 0
    weightSum = 0
    for _ in range(int(input())):
        lvl, score = input().split()
        score = int(score)
        if lvl == 'LOW': lvl = 1
        elif lvl == 'MEDIUM': lvl = 2
        else: lvl = 3
        sum += score * lvl
        weightSum += lvl
    print(f'{math.floor(sum/weightSum*10+0.5)}')