import sys
input = lambda: sys.stdin.readline().rstrip()
import math
#import string
#import re

for _ in range(int(input())):
    EX, EY, MX, MY = map(float, input().split())
    a = math.dist((EX, EY), (0, 0))
    b = math.dist((EX, EY), (MX, MY))
    c = math.dist((MX, MY), (0, 0))
    angle_cos = math.degrees(math.acos((math.pow(a, 2) + math.pow(b, 2) - math.pow(c, 2)) / (2 * a * b)))

    if angle_cos < 2:
        print('VACATION')
    else:
        print('WORKING HARD')