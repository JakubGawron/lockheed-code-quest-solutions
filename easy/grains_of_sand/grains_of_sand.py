import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    sum = 0
    for _ in range(int(input())):
        sum += int(input())
    print(sum)