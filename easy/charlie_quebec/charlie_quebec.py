import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re
from string import ascii_uppercase

phonetic = ['Alpha','Bravo','Charlie','Delta','Echo','Foxtrot','Golf','Hotel','India','Juliet','Kilo','Lima','Mike','November','Oscar','Papa','Quebec','Romeo','Sierra','Tango','Uniform','Victor','Whiskey','Xray','Yankee','Zulu']

cases = int(input())
for _ in range(cases):
    lines = int(input())
    for _ in range(lines):
        text = input().upper().split(' ')
        answer = [[phonetic[ascii_uppercase.index(letter)] for letter in word] for word in text]
        print(' '.join(['-'.join(word) for word in answer]))