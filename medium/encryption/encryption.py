import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
import string
#import re

for _ in range(int(input())):
    mode = input()
    alphabet, letters_map = string.ascii_lowercase, input()
    if mode == 'DECRYPT':
        alphabet, letters_map = letters_map, alphabet
    
    for _ in range(int(input())):
        message = input()
        capslock = [letter.isupper() for letter in message]
        for i, letter in enumerate(message.lower()):
            base = ' '
            try:
                base = letters_map[alphabet.index(letter)]
            except ValueError: pass
            print(base.upper() if capslock[i] else base, end='')
        print()