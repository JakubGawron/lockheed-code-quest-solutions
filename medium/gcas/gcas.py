import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    altitudes, elevations = [0], [0, 0]
    N = int(input())
    for _ in range(N):
        a, e = map(int, input().split(','))
        altitudes.append(a)
        elevations.append(e)
    
    for i in range(1, N + 1):
        if 2 * altitudes[i] - altitudes[i - 1] <= elevations[i + 1]:
            print('PULL UP!')
        elif altitudes[i] - elevations[i] <= 500:
            print('Low Altitude!')
        else:
            print('ok')