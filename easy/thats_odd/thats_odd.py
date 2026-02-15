import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    num = int(input())
    if num % 2:
        print('ODD')
    else:
        print('EVEN')