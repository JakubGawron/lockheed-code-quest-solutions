import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    line1 = set(input().split(','))
    line2 = set(input().split(','))

    print(','.join(sorted(line1-line2)))
    print(','.join(sorted(line1.intersection(line2))))
    print(','.join(sorted(line2-line1)))