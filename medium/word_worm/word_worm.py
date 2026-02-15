import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1),]

def dfs(grid, word, y, x, R, C, i = 1):
    if i == len(word): return True
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == word[i]:
            if dfs(grid, word, ny, nx, R, C, i + 1):
                return True
    return False


def exists(grid, word, R, C):
    for y in range(R):
        for x in range(C):
            if grid[y][x] == word[0]:
                if dfs(grid, word, y, x, R, C):
                    return True
    return False

for _ in range(int(input())):
    R, C = map(int, input().split())
    grid = [input().split() for _ in range(R)]

    for _ in range(int(input())):
        word = input()
        if exists(grid, word, R, C):
            print(word)