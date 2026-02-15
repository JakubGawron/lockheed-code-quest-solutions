import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    N, L, A, H = map(float, input().split())
    N = int(N)
    temperatures = list(map(float, input().split()))

    if any(temperature < L for temperature in temperatures):
        print('TOO COOL')
    elif any(temperature > H for temperature in temperatures):
        print('TOO HOT')
    elif sum(temperatures) / N > A:
        print('WARNING')
    else:
        print('OK')