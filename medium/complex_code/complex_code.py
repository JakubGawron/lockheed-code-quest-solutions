import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    L, C, N = map(int, input().split())
    cyclomatic, nesting = 1, [0]
    for _ in range(L):
        pseudocode = input()
        if 'If' in pseudocode[:2]:
            cyclomatic += 1
        elif '{' in pseudocode[:1]:
            nesting.append(nesting[-1]+1)
        elif '}' in pseudocode[:1]:
            nesting.append(nesting[-1]-1)

    nesting = max(nesting)
    print(cyclomatic, nesting, 'PASS' if cyclomatic <= C and nesting <= N else 'FAIL')