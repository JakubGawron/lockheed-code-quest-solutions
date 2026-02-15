import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
import string
#import re

alp = string.ascii_lowercase
for _ in range(int(input())):
    shift = int(input())
    cipher = input()
    key = alp[shift:] + alp[:shift]
    for letter in cipher:
        if letter != ' ':
            letter = alp[key.index(letter)]
        print(letter, end='')
    print()