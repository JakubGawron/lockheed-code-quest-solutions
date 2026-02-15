import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
import re

for _ in range(int(input())):
    hex_msg = ''.join(input())
    if re.fullmatch(r'[A-Za-z0-9 .,:\[\]]+', bytes.fromhex(hex_msg).decode()):
        print('VALID')
    else:
        print('INVALID')