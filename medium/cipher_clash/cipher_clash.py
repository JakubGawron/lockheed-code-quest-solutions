import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
import re

for _ in range(int(input())):
    line = input()
    match = re.search(r'\[(\d+)\,(\d+)\]\s"(.*)"\s"(.*)"', line)
    x, y, text1, text2 = match.groups()
    x, y, text1, text2 = int(x), int(y), text1.split(), text2.split()
    if sorted(text1[x-1]) == sorted(text2[y-1]):
        print('Verified')
    else:
        print('Intercepted')