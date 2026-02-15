import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    turkeys, goats, horses = map(int, input().split())
    print(turkeys * 2 + (goats + horses) * 4)