import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
import re

for _ in range(int(input())):
    word = input()
    len_word = len(word)
    if 5 <= len_word <= 32 and re.fullmatch(r'[A-Za-z]+', word):
        print(word)
        rev_word = word[::-1]
        inside = len_word - 2
        fill = ' ' * inside
        for i in range(inside):
            print(word[i + 1] + fill + rev_word[i + 1])
        print(rev_word)
    else:
        print('Not a Calliframe')