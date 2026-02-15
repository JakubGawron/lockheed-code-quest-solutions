import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    word, target = input().split()
    if word[0] == target[0] and word[-1] == target[-1] and set(word) == set(target):
        print(target)
    else:
        print(word)