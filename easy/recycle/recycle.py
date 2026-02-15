import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    aluminium, plastic, glass = map(int, input().split())
    aluminium = aluminium * 31
    plastic = plastic * 15
    glass = glass / 2
    sum = aluminium * 0.05 + plastic * 0.1 + glass * 0.2
    print(f'${sum:.2f}')