import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    cords = list(map(float, input().split()))
    for i in range(3):
        cords[i] = f'{(cords[i]-180)%360:.2f}'.zfill(6)
    print(' '.join(cords))