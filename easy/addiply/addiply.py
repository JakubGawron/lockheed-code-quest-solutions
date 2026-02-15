import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

cases = int(input())
for _ in range(cases):
    a, b = map(int, input())
    print(a + b, a * b)