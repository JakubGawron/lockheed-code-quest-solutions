import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    small, big, want = map(int, input().split())

    sum = 0
    for b in range(1, big+1):
        if b*5 <= want:
            sum=b*5
        else: 
            break
    
    if sum + small >= want:
        print('true')
    else:
        print('false')