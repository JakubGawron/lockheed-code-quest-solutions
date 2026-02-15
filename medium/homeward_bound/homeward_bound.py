import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    X = int(input())
    dict1 = dict([input().split() for _ in range(X)])
    dict2 = dict([(b, a) for a, b in dict1.items()])
    start = (dict2.keys() - dict1.keys()).pop()
    print(start)
    for i in range(X):
            start = dict2[start]
            print(start)