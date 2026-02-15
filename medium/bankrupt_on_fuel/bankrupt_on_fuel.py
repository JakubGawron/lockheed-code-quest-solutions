import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
import math
#import string
#import re

for _ in range(int(input())):
    fuelLeft, N = map(int, input().split())
    capacities = list(map(int, input().split()))
    contents = [0] * N
    unfilledTanks = N
    highestLevel = 0
    while fuelLeft >= unfilledTanks:
        for i in range(N):
            if contents[i] < capacities[i]:
                contents[i] += 1
                fuelLeft -= 1
                if contents[i] == capacities[i]:
                    unfilledTanks -= 1
        highestLevel += 1
    
    for i in range(N):
        if i != 0: print(' ', end='')
        if contents[i] == capacities[i]:
            print(contents[i], end='')
        else:
            gcd = math.gcd(fuelLeft, unfilledTanks)
            denominator = int(unfilledTanks / gcd)
            if denominator == 1:
                print(contents[i], end='')
            else:
                numerator = int((highestLevel * denominator) + (fuelLeft / gcd))
                print(f'{numerator}/{denominator}', end='')
    print()