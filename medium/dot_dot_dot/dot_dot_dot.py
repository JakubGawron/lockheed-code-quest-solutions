import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
import string
#import re

for _ in range(int(input())):
    word = input()
    dots = 0
    for letter in word:
        dots += string.ascii_lowercase.index(letter) + 1
    print(dots)