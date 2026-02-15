import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    text = input()
    if 'red' in text:
        print('red')
    elif 'blue' in text:
        print('blue')
    else:
        print('no color found')