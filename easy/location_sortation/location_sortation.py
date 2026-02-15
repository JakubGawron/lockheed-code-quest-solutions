import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

list = []
for _ in range(int(input())):
    country = input()
    list.append(country)

list.sort()
for country in list:
    print(country)