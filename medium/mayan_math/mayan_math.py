import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

base20 = {
    0: '0',
    1: '.',
    2: '..',
    3: '...',
    4: '....',
    5: '-',
    6: '.-',
    7: '..-',
    8: '...-',
    9: '....-',
    10: '--',
    11: '.--',
    12: '..--',
    13: '...--',
    14: '....--',
    15: '---',
    16: '.---',
    17: '..---',
    18: '...---',
    19: '....---',
}

def getMaxStack(n, stack = 1):
    if n < 20 ** stack:
        return stack
    return getMaxStack(n, stack + 1)

def toBase20(n):
    base = []
    for level in range(getMaxStack(n) - 1, -1, -1):
        num = n // (20 ** level)
        base.append(num)
        n %= 20 ** level
    return ' '.join([base20[layer] for layer in base])

for _ in range(int(input())):
    num = int(input())
    print(toBase20(num))