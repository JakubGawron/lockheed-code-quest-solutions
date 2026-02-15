import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

def get_score(throws, i):
    if throws[i] == '-':
        return 0
    elif throws[i] == 'X':
        return 10
    elif throws[i] == '/':
        return 10 - get_score(throws, i - 1)
    return int(throws[i])

for _ in range(int(input())):
    frames = input().split(',')
    throws = [f for frame in frames for f in frame]
    total = i = 0

    for frame in range(10):
        if throws[i] == 'X':
            total += 10 + get_score(throws, i + 1) + get_score(throws, i + 2)
            i += 1
        elif throws[i + 1] == '/':
            total += 10 + get_score(throws, i + 2)
            i += 2
        else:
            total += get_score(throws, i) + get_score(throws, i + 1)
            i += 2

    print(total)