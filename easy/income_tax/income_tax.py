import sys
input = lambda: sys.stdin.readline().rstrip()
import math
#import string
#import re

for _ in range(int(input())):
    income = int(input())
    if income <= 11000:
        tax = income * 0.1
    elif income <= 44725:
        tax = income * 0.12
    elif income <= 95375:
        tax = income * 0.22
    elif income <= 182100:
        tax = income * 0.24
    elif income <= 231250:
        tax = income * 0.32
    elif income <= 578125:
        tax = income * 0.35
    else:
        tax = income * 0.37
    print(math.floor(tax + 0.5))