import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    amount  = float(input()[1:])
    print(f'Total of the bill: ${amount:.2f}')
    print(f'15% = ${(amount * 0.15):.2f}')
    print(f'18% = ${(amount * 0.18):.2f}')
    print(f'20% = ${(amount * 0.20):.2f}')