import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
import re

def repl(match):
    return data[match.group(1)]

for _ in range(int(input())):
    D, T = map(int, input().split())
    data = dict(input().split(': ', maxsplit=1) for _ in range(D))
    text = '\n'.join([input() for _ in range(T)])
    result = re.sub(r'\[([\w\s]+)\]', repl, text)
    print(result)