import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    directions = input()
    if len(directions) % 2 != 0:
        print('FALSE')
    else:
        x, y = 0, 0
        for move in directions:
            if move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
            else:
                y += 1
        
        if x == 0 and y == 0:
            print('TRUE')
        else:
            print('FALSE')