import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

dict = {
    'yellow': None,
    'red': None,
    'blue': None,

    'red-orange': ['red', 'yellow'],
    'orange': ['red', 'yellow'],
    'yellow-orange': ['red', 'yellow'],

    'yellow-green': ['blue', 'yellow'],
    'green': ['blue', 'yellow'],
    'blue-green': ['blue', 'yellow'],

    'blue-violet': ['blue', 'red'],
    'violet': ['blue', 'red'],
    'red-violet': ['blue', 'red'],
}

for _ in range(int(input())):
    color = input()
    needed = dict[color]
    if needed:
        print(f'In order to make {color}, {needed[0]} and {needed[1]} must be mixed.')
    else:
        print(f'No colors need to be mixed to make {color}.')