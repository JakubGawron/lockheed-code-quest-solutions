import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    word = input()

    total = 0
    for letter in word:
        value = 1
        if letter in 'DG':
            value = 2
        elif letter in 'BCMP':
            value = 3
        elif letter in 'FHVWY':
            value = 4
        elif letter in 'K':
            value = 5
        elif letter in 'JX':
            value = 8
        elif letter in 'QZ':
            value = 10
        total += value
        print(f'{letter}={value}')
    print(f'TOTAL={total}')