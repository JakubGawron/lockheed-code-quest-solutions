import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

def multiplyMatrices(a, b):
    b = list(zip(*b))
    return [[str(sum(x*y for x, y in zip(row, col))) for col in b] for row in a]


for _ in range(int(input())):
    N, M, P, Q = map(int, input().split())
    a = [tuple(map(int, input().split())) for _ in range(N)]
    b = [tuple(map(int, input().split())) for _ in range(P)]
    if M == P:
        c = multiplyMatrices(a, b)
        print('\n'.join([' '.join(row) for row in c]))
    else:
        print('undefined')