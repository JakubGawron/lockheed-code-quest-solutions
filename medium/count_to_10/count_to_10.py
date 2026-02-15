import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    max = int(input())
    for i in range(2**(max)):
        print(f'{i:b}'.zfill(max))