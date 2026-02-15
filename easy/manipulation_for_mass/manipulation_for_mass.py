import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    den, vol = map(float, input().split())
    print(f'{den*vol:.2f}')