import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    nums = list(map(int, input().split(',')))
    nums.sort()
    print(','.join(map(str, nums)))