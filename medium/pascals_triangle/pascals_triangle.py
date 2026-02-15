import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
import math
#import string
#import re

for _ in range(int(input())):
    i = int(input())
    print(math.comb(i, i // 2))