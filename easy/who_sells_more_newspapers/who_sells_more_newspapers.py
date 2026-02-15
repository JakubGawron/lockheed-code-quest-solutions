import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    Time, Herald = map(int, input().split())
    if Time == Herald:
        print('Times and Herald have the same number of subscribers')
    elif Time > Herald:
        print(f'Times has {Time-Herald} more subscribers')
    else:
        print(f'Herald has {Herald-Time} more subscribers')