import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    num = input()[:-2]

    end = 'th'
    if not num.endswith('11') and not num.endswith('12') and not num.endswith('13'):
        if num[-1] == '1': end = 'st'
        elif num[-1] == '2': end = 'nd'
        elif num[-1] == '3': end = 'rd'
    print(num+end)