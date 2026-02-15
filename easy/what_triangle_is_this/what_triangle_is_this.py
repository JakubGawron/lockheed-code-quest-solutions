import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    a, b, c = map(int, input().split(', '))

    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print('Equilateral')
        elif a == b or b == c or c == a:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Not a Triangle')