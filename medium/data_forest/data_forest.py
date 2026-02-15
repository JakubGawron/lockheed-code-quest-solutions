import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
import math
#import string
#import re

def bst(numbers, d, levels):
    if not numbers:
        return
    mid = len(numbers) // 2
    levels[d].append(numbers[mid].rjust(3))
    bst(numbers[:mid], d + 1, levels)
    bst(numbers[mid + 1:], d + 1, levels)

for _ in range(int(input())):
    numbers = sorted(input().split())
    N = int(math.log(len(numbers) + 1, 2))
    levels = [[] for _ in range(N)]
    bst(numbers, 0, levels)

    sep = 1
    for i in range(N):
        start = 2 ** (N - i - 1) - 1
        print('   ' * start + ('   ' * sep).join(levels[i]))
        sep = start