import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
import math
#import string
#import re

for _ in range(int(input())):
    n = int(input())

    x1 = 5 * n ** 2
    x2 = x1 - 4
    x1 += 4

    if int(math.sqrt(x1))**2 == x1 or int(math.sqrt(x2))**2 == x2:
        print('TRUE')
    else:
        print('FALSE')