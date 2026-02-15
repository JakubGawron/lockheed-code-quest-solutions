import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
import re

for _ in range(int(input())):
    text = input()

    h = m = s = '00'
    for part in re.split('(?: |,|and)+', text):
        time_part = part[-1]
        part = part[:-1].zfill(2)
        if time_part == 'h': h = part
        elif time_part == 'm': m = part
        else: s = part
    print(f'{h}:{m}:{s}')