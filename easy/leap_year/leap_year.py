import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    for _ in range(int(input())):
        year = int(input())

        if year < 1582: print('No')
        elif year % 4 != 0: print('No')
        elif year % 100 != 0: print('Yes')
        elif year % 400 != 0: print('No')
        else: print('Yes')