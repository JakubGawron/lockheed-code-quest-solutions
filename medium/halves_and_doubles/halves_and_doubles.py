import sys
input = lambda: sys.stdin.readline().rstrip()
import math
#import string
#import re

def output(x, y, r):
    isEven = '' if x % 2 else ' ***'
    print(f'{x}{'*' if r > x else ''} {y}{isEven}')
    return 0 if isEven else y

for _ in range(int(input())):
    x, y = map(int, input().split())
    r, ans = 0, 0
    ans += output(x, y, r)
    while x != 1:
        r = x / 2
        x = math.floor(r)
        y *= 2
        ans += output(x, y, r)
    print(ans)
        