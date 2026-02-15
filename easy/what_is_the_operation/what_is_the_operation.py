import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    a, b, target = map(int , input().split())

    if a + b == target:
        print('Addition')
    elif a - b == target:
        print('Subtraction')
    elif a * b == target:
        print('Multiplication')
    elif b != 0 and a // b == target:
        print('Division')
    else:
        print('Modulo')