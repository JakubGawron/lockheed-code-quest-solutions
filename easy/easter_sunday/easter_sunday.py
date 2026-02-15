import sys
input = lambda: sys.stdin.readline().rstrip()
import math
#import string
#import re

for _ in range(int(input())):
    y = int(input())
    a = y % 19
    b = y % 4
    c = y % 7
    k = math.floor(y / 100)
    p = math.floor((13 + 8 * k) / 25)
    q = math.floor(k / 4)
    m = (15 - p + k - q) % 30
    n = (4 + k - q) % 7
    d = (19 * a + m) % 30
    e = (2 * b + 4 * c + 6 * d + n) % 7
    f = (11 * m + 11) % 30

    day = 22 + d + e
    month = '03'
    if day > 31:
        day -= 31
        month = '04'

    if d == 28 and e == 6 and f < 19:
        day = 18
    elif d == 29 and e == 6:
        day = 19

    print(f'{y}/{month}/{str(day).zfill(2)}')
        
