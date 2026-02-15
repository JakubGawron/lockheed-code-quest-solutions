import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
import math
#import string
#import re

for _ in range(int(input())):
    X1, Y1, X2, Y2, W, N = map(float, input().split())
    for _ in range(int(N)):
        X, Y = map(float, input().split())

        d = round(math.sqrt((X-X1)**2+(Y-Y1)**2) + math.sqrt((X-X2)**2+(Y-Y2)**2), 3)

        if d <= W: print(1)
        else: print(0)