import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
import string
#import re

alphabet = string.ascii_uppercase
for _ in range(int(input())):
    A, W = map(int, input().split())
    prices = [((A+i-1)%26)+1 for i in range(26)]

    for _ in range(W):
        word = input()
        price = sum([prices[alphabet.index(letter)] for letter in word])
        if price == 100:
            print(f'WINNER {A}: {word}')