import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    list = input().split()
    R = list.count('R')
    P = list.count('P')
    S = list.count('S')
    if R == 1 and P == 0:
        print('ROCK')
    elif P == 1 and S == 0:
        print('PAPER')
    elif S == 1 and R == 0:
        print('SCISSORS')
    else:
        print('NO WINNER')