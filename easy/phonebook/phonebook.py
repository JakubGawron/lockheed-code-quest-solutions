import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    phone, format = input().split()
    if format == 'PARENTHESES':
        print(f'({phone[:3]}) {phone[3:6]}-{phone[6:]}')
    elif format == 'DASHES':
        print(f'{phone[:3]}-{phone[3:6]}-{phone[6:]}')
    elif format == 'PERIODS':
        print(f'{phone[:3]}.{phone[3:6]}.{phone[6:]}')