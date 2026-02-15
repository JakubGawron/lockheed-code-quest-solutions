import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    V, X = map(float, input().split(':'))
    if X <= V: print('SWERVE')
    elif X <= V*5: print('BRAKE')
    else: print('SAFE')