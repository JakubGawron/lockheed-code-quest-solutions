import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

def wrapOneRow(text, width_limit):
    if len(text) <= width_limit:
        return text, ''
    elif ' ' in text[width_limit - 1:width_limit + 1]:
        row = text[:width_limit].rstrip()
        remaining = text[width_limit:].lstrip()
        return row, remaining
    else:
        l = text[:width_limit].rsplit(maxsplit=1)
        if len(l) == 1:
            return None, None
        row, remaining = text[:width_limit].rsplit(maxsplit=1)
        remaining += text[width_limit:]
        return row, remaining

for _ in range(int(input())):
    width_limit, height_limit = map(int, input().split())
    text = input()
    
    current_height = 0
    rows = []
    
    while text:
        if current_height >= height_limit:
            print('WILL NOT FIT')
            break
        
        row, text = wrapOneRow(text, width_limit)
        if not row:
            print('WILL NOT FIT')
            break
        
        rows.append(row)
        current_height += 1
    else:
        print('\n'.join(rows))
