import sys
input = lambda: sys.stdin.readline().rstrip()
import math
#import string
#import re

for _ in range(int(input())):
    replacements = int(input())
    o_model, o_rate = input().split(maxsplit=1)
    o_rate = sum(map(int, o_rate.split()))
    minModel = None
    minRate = None
    for _ in range(replacements):
        model, rate = input().split(maxsplit=1)
        rate = sum(map(int, rate.split()))
        if not minRate or minRate > rate:
            minModel = model
            minRate = rate
    
    if minRate < float(f'{o_rate*0.8:.3f}'):
        print(minModel, minRate)
    else:
        print(o_model, o_rate)