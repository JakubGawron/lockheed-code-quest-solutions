import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    print(''.join(sorted(input().split(), key=lambda x: x * 10, reverse=True)))