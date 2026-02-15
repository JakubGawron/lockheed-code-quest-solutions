import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    PY, PX = map(int, input().split())
    list = [['10' for _ in range(20)] for _ in range(20)]
    
    for y in range(20):
        for x in range(20):
            if PX == x and PY == y:
                list[y][x] = '100'
            elif PX-1 <= x <= PX+1 and PY-1 <= y <= PY+1:
                list[y][x] = '50'
            elif PX-2 <= x <= PX+2 and PY-2 <= y <= PY+2:
                list[y][x] = '25'

    for row in list:
        print(' '.join(row))