import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    G1, G2 = input().split()
    if G1 == G2:
        print('true')
    else:
        print('false')