import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    cass, lead = map(int, input().split())
    if cass == lead:
        print('Cassowary Craft and Lead Balloons Ltd sold the same number of aircraft')
    elif cass > lead:
        print(f'Cassowary Craft sold {cass-lead} more aircraft')
    else:
        print(f'Lead Balloons Ltd sold {lead-cass} more aircraft')