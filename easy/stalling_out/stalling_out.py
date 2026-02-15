import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    critical, port, starboard = map(float, input().split())
    if abs(port-starboard) > 5:
        print('WARNING')
    elif (port+starboard)/2-critical >= 2:
        print('ALARM')
    else:
        print('OK')