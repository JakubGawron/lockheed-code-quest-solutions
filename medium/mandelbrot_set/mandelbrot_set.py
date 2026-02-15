import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

def mandelBrot(Z, c, n = 0):
    if n >= 51:
        return 51
    elif abs(Z) >= 100:
        return n
    return mandelBrot(Z*Z + c, c, n + 1)

def getColor(n):
    if n <= 10:
        return 'RED'
    elif n <= 20:
        return 'ORANGE'
    elif n <= 30:
        return 'YELLOW'
    elif n <= 40:
        return 'GREEN'
    elif n <= 50:
        return 'BLUE'
    else:
        return 'BLACK'

for _ in range(int(input())):
    a, b = map(float, input().split())
    Z = complex(0, 0)
    c = complex(a, b)
    n = mandelBrot(Z, c)
    print(f'{a}+{b}i', getColor(n))