import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    R, W, H = map(float, input().split())
    for x in range(int(W)+1):
        for y in range(int(H)+1):
                if x**2 + y**2 > R**2:
                    print(f'{x},{y}')