import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    result = 'VALID'
    try:
        addr = list(map(int, input().split('.')))
        if len(addr) != 4:
            result = 'INVALID'
        else:
            for num in addr:
                if num > 255 or num < 0:
                    result = 'INVALID'
                    break
    except Exception:
        result = 'INVALID'
    print(result)