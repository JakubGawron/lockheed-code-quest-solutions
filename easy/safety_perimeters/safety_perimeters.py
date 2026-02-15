import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
import math
#import string
#import re

for _ in range(int(input())):
    N = int(input())
    XR, YR, safeDistance = map(int, input().split())
    for _ in range(N):
        X, Y = map(int, input().split())
        d = math.sqrt((X-XR)**2+(Y-YR)**2)
        text = 'DANGER' if d <= safeDistance else 'SAFE'
        print(f'({X},{Y}) {text}')