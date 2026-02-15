import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

cases = int(input())
for _ in range(cases):
    str = input()
    print(str.count('a') + str.count('e') + str.count('i') + str.count('o') + str.count('u'))