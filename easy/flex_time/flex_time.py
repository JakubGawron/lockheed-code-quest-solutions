import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    hours = 0
    for _ in range(int(input())):
        hours += sum(map(int, input().split()))
    print(hours - 40)