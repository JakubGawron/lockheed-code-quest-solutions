import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
import math
#import string
#import re

for _ in range(int(input())):
    d, full, P, speed, capacity, voltage, distance = map(float, input().split())

    C = math.pi * d
    distance = distance * 100
    reqRot = distance/C
    reqRev = reqRot * full

    time =  reqRev / speed
    totalW = reqRev * P
    if (totalW / voltage * time / 60) <= capacity:
        print(f'Success {time:.4f}')
    else:
        print('Fail')