import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

from decimal import Decimal, ROUND_HALF_UP
def halfUpRound(value, q = 0, type = 'string'):
    rounded = Decimal(str(value)).quantize(Decimal('1').scaleb(-q), rounding=ROUND_HALF_UP)
    if rounded == Decimal('0'):
        rounded = abs(rounded)
    if type == 'string':
        return format(rounded, f'.{q}f')
    return float(rounded)

def getGradeLetter(grade):
    grade = float(grade)
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

for _ in range(int(input())):
    X, corrects = input().split()
    count = len(corrects)

    for _ in range(int(X)):
        name, grades = input().split()
        correct = sum([grade is correct for correct, grade in zip(corrects, grades)])
        grade = halfUpRound(correct / count * 100, 1)

        print(name, grade + '%', getGradeLetter(grade))