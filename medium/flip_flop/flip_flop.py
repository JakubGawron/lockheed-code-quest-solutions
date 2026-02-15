import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    R, C = map(int, input().split())
    print('\n'.join(','.join(row) for row in zip(*[input().split(',') for _ in range(R)])))