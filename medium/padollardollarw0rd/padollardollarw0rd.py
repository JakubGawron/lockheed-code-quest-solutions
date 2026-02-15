import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
import re

patterns = [
    r'[A-Z]',
    r'[a-z]',
    r'\d',
    r'[\W_-]'
]

for _ in range(int(input())):
    password = input()
    if len(password) >= 8 and sum([bool(re.search(pattern, password)) for pattern in patterns]) >= 3 and not bool(re.search(r'(.)\1\1', password)):
        print('VALID')
    else:
        print('INVALID')