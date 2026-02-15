import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    grade = int(input())

    if grade >= 70:
        print('PASS')
    else:
        print('FAIL')