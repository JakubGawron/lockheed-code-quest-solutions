import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

directions = 'NESW'
for _ in range(int(input())):
    x, y, facing, instructions = input().split()
    x, y = int(x), int(y)
    for instruction in instructions:
        if instruction == 'R':
            facing = directions[(directions.index(facing) + 1) % 4]
        elif instruction == 'L':
            facing = directions[(directions.index(facing) - 1) % 4]
        else:
            if facing == 'N':
                y += 1
            elif facing == 'E':
                x += 1
            elif facing == 'S':
                y -= 1
            elif facing == 'W':
                x -= 1
    print(x, y, facing)