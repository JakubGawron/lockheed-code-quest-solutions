import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

rank = {char: i for i, char in enumerate('/.-ABCDEFGHIJKLMNPQRSTUVWXYZ0123456789')}
rank['O'] = 28

def getRankOfPart(parts):
    return [rank[part] for part in parts]

for _ in range(int(input())): 
    parts = [input() for _ in range(int(input()))]
    print('\n'.join(sorted(parts, key=getRankOfPart)))