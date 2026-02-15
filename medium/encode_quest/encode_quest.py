import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
import string
#import re

alphabet = string.ascii_uppercase
for _ in range(int(input())):
    plaintext = input()
    keyword = input()

    vinegre = []
    for letter in keyword:
        i = alphabet.index(letter)
        vinegre.append(alphabet[i:] + alphabet[:i])
    
    c = 0
    for letter in plaintext:
        if letter == ' ': 
            print(' ', end='')
        else:
            print(vinegre[c % len(keyword)][alphabet.index(letter)], end='')
            c += 1
    print()