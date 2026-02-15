import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
import re

for _ in range(int(input())):
    message = [input() for _ in range(int(input()))]
    Y, X = map(int, input().split(','))
    cover = [input() for _ in range(int(input()))]
    message = message[Y:]
    indexes = [[match.start() for match in re.finditer('O', row)] for row in cover]
    print(''.join(sum([[message[y][X + i] for i in row] for y, row in enumerate(indexes)], [])))