import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    X, Y = map(int, input().split())
    all, working = set(), set()
    for _ in range(X):
        all.add(input())
    for _ in range(Y):
        working.add(input())
    for syst in sorted(all-working, key=str.lower):
        print(syst)