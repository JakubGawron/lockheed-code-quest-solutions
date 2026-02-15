import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
import string
#import re

def reverse_word(word):
    capslock = [letter.isupper() for letter in word]
    word = word.lower()[::-1]
    return ''.join([word[i].upper() if capslock[i] else word[i] for i in range(len(word))])

alph = string.ascii_lowercase + string.ascii_uppercase
for _ in range(int(input())):
    sentence = input()
    word = ''
    for letter in sentence:
        if letter in alph:
            word += letter
        else:
            print(reverse_word(word), end='')
            word = ''
            print(letter, end='')
    print(reverse_word(word), end='')
    print()