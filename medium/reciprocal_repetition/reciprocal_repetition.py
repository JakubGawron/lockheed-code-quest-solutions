import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    num = int(input())

    r, dec, seen, pos = 1, '', {}, 0
    while r != 0:
        if r in seen:
            dec = dec[seen[r]:]
            break
        seen[r] = pos
        r *= 10
        dec += str(r // num)
        r %= num
        pos += 1
    else:
        dec = '0'

    print(dec)