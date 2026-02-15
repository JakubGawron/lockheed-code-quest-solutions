import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
import math
#import string
import re

for _ in range(int(input())):
    lengths = [[], []]
    U = int(input())
    lengths[0] = list(map(int, input().split()))
    L = int(input())
    lengths[1] = list(map(int, input().split()))

    N = math.ceil((sum(lengths[0]) + sum(lengths[1])) / 80)
    encoded = ''.join(input() for _ in range(N))

    texts = [
        ''.join(re.findall(r'[A-Z-]', encoded)).replace('-', ' '), 
        ''.join(re.findall(r'[a-z=]', encoded)).replace('=', ' ')
    ]

    for i in range(2):
        if i == 1: print()
        start = 0
        for length in lengths[i]:
            print(texts[i][start:start + length])
            start += length