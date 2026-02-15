import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

vovels = 'aeiou'
for _ in range(int(input())):
    cipher = input()
    skip = None
    for i, letter in enumerate(cipher):
        if letter in vovels and i != skip:
            print(cipher[i+1], end='')
            skip = i+1
    print()