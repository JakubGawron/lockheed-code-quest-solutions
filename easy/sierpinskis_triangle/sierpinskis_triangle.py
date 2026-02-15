import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    W, N = map(float, input().split())
    triangles = int(3 ** N)
    w = W / (2 ** N)
    areaTriangle = 3**(1/2)/4*w**2
    print(f'{triangles} {areaTriangle*triangles:.2f}')