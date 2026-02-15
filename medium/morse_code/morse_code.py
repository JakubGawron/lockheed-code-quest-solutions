import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

def code(text, dict, sep):
    return sep.join([' ' if part == ' ' else dict[part] for part in text])

def encode(text, dict, seps):
    return seps[1].join([seps[0].join([dict[letter] for letter in word]) for word in text.split()])

def decode(code, dict, seps):
    return ' '.join([''.join([dict[letter] for letter in word.split(seps[0])]) for word in code.split(seps[1])])

for _ in range(int(input())):
    dict_encode = dict([input().split(maxsplit=1) for _ in range(26)])
    dict_decode = dict(zip(dict_encode.values(), dict_encode.keys()))
    seps = (' ' * 3), (' ' * 7)
    print(encode(input(), dict_encode, seps))
    print(decode(input(), dict_decode, seps))