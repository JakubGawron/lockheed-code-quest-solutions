import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    C, T = map(int, input().split())
    budget = {}

    for _ in range(C):
        category, amount = input().split()
        amount = int(amount)
        budget[category] = amount

    for _ in range(T):
        category, type, amount = input().split()
        amount = int(amount)

        if type == '+':
            print('YES')
            budget[category] += amount
        elif amount <= budget[category]:
            print('YES')
            budget[category] -= amount
        else:
            print('NO')