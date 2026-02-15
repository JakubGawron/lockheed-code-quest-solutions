import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
import string
#import re
import itertools

alphabet = string.ascii_lowercase
for _ in range(int(input())):
    cipher = input().lower()
    shift = itertools.cycle(map(int, input().split()))
    directions = itertools.cycle(map(int, input().split()))

    for letter in cipher:
        if letter in alphabet:
            direction = 1 if next(directions) == 0 else -1 
            letter = alphabet[(alphabet.index(letter) + direction * next(shift)) % 26]
        print(letter, end='')
    print()