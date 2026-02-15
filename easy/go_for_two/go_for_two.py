import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re
dec = [-15, -13, -11, -10, -8, -5, -4, -2, 1, 5, 12]

for _ in range(int(input())):
    M, O = map(int, input().split())
    margin = M - O

    if margin in dec:
        print(2)
    else:
        print(1)