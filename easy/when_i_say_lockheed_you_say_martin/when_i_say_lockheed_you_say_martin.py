import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    num = int(input())
    mod3 = 1 if num % 3 == 0 else 0
    mod7 =1 if num % 7 == 0 else 0
    if mod3 and mod7:
        print('LOCKHEEDMARTIN')
    elif mod3:
        print('LOCKHEED')
    elif mod7:
        print('MARTIN')
    else:
        print(num)