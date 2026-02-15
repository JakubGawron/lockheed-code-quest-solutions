import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    bits = int(input())
    values = list(map(int, input().split()))
    maximum = 2 ** bits - 1
    if any(value > maximum for value in values):
        print(maximum, 'FALSE')
    else:
        print(maximum, 'TRUE')