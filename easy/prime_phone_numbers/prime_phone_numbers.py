import sys
input = lambda: sys.stdin.readline().rstrip()
import math
#import string
import re

for _ in range(int(input())):
    number = input()
    abc = re.match(r'\((\d{3})\)(\d{3})-(\d{4})', number)
    a, b, c = map(int, abc.groups())
    
    if \
    math.gcd(a, b) == 1 and \
    math.gcd(b, c) == 1 and \
    math.gcd(a, c) == 1:
        print('TRUE')
    else:
        print('FALSE')
