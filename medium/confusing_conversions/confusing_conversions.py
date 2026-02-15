import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    function, params = input().split(maxsplit=1)
    if function == 'formatHeight':
        X, Y = params.split()
        print(f"{X}'{Y}\"")
    elif function == 'formatDate':
        X, Y, Z = params.split()
        print(f"{X}{Y.zfill(2)}{Z.zfill(2)}")
    else:
        print(params.replace(' ', ','))