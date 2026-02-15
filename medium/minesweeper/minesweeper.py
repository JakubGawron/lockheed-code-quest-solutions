import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    rows, cols, B = map(int, input().split())
    grid = [[0] * cols for _ in range(rows)]

    for _ in range(B):
        y, x = map(int, input().split())
        grid[y][x] = '*'

        for sy in range(-1, 2):
            for sx in range(-1, 2):
                ny, nx = y + sy, x + sx
                if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] != '*':
                    grid[ny][nx] += 1
    print('\n'.join([''.join(map(str, row)) for row in grid]))
