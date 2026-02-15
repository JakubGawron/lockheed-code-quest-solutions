import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    num_values = int(input())
    list = []
    for _ in range(num_values):
        list.append(float(sys.stdin.readline().strip()))
    
    mini = min(list)
    maxi = max(list)
    for input in list:
        print(round(((input-mini)/(maxi-mini))*255))