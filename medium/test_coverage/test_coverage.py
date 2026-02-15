import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    N = int(input())
    A = set(input().split(','))
    B = set(x for _ in range(N) for x in input().split(',')[1:])
    result = list(A - B)
    if result:
        print(','.join(sorted(result)))
    else:
        print('FULL COVERAGE')