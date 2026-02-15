import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    num = int(input())
    print('POSITIVE' if num > 0 else 'NEGATIVE')