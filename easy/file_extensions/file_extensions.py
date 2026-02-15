import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

files = {}
for _ in range(int(input())):
    file = input()
    ext = file.split('.')[1]
    if ext not in files:
        files[ext] = 1
    else:
        files[ext] += 1

for key, value in files.items():
    print(key, value)