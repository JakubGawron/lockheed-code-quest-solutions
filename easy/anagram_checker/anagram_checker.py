import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    text = input()
    n = ''
    a, b = text.split('|')
    if sorted(a) != sorted(b) or a == b: n = 'NOT AN '
    print(text + f' = {n}ANAGRAM')