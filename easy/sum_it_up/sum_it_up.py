import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a != b:
        print(a+b)
    else:
        print((a+b)*2)