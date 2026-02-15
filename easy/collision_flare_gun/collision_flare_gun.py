import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    v1, m1, v2, m2 = map(float, input().split(','))
    V = (m1*v1+m2*v2)/(m1+m2)
    print(f'{round(V, 2):.2f}')