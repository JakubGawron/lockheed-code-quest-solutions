import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    R, C = map(int, input().split(','))
    r1, c1 = map(int, input().split(','))
    r2, c2 = map(int, input().split(','))
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print('Yes')
    else:
        print('No')