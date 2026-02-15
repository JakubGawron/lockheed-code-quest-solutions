import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    ISBN = input()
    S = 0
    for i in range(9):
        S += int(ISBN[i]) * (10 - i)
    
    check = 10 if ISBN[-1] == 'X' else int(ISBN[-1])

    if (S+check) % 11 == 0:
        print('VALID')
    else:
        print('INVALID')