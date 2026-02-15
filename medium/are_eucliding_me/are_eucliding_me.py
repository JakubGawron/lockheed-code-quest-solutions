import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

def gcd(minuend, subtrahend):
    diff = minuend - subtrahend
    print(f'{minuend}-{subtrahend}={diff}')
    if diff == 0:
        if minuend == 1:
            print('COPRIME')
        else:
            print('NOT COPRIME')
        return
    minuend, subtrahend = sorted([subtrahend, diff], reverse=True)
    gcd(minuend, subtrahend) 

for _ in range(int(input())):
    minuend, subtrahend = sorted(map(int, input().split(',')), reverse=True)
    gcd(minuend, subtrahend)