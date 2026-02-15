import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    max = int(input())
    sens = set(map(int, input().split()))
    print((set(range(1, max+1))-sens).pop())