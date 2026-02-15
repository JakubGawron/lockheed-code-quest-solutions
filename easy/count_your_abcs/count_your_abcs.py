import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re
from string import ascii_uppercase
 
for _ in range(int(input())):
    text = input()
    list = []
    for letter in ascii_uppercase:
        list.append(text.count(letter))
    print(max(list))