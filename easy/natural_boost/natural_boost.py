import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
import math
#import string
#import re

v = (2 * math.pi * 6370000)/86400

for _ in range(int(input())):
    latitude = float(input())
    print(math.floor(math.cos(math.radians(latitude))*v))