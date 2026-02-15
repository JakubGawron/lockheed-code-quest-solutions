import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    binary = input().translate(str.maketrans({'G': '1', 'C': '1', 'A': '0', 'T': '0'}))
    print(''.join(chr(int(binary[i:i + 7], 2)) for i in range(0, len(binary), 7)))