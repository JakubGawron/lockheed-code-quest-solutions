import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

def game_outcome(grid):
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != '-':
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] != '-':
            return grid[0][i]

    if grid[0][0] == grid[1][1] == grid[2][2] != '-':
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != '-':
        return grid[0][2]
    return

for _ in range(int(input())):
    board = input()
    grid = [board[i:i+3] for i in range(0, len(board), 3)]
    result = game_outcome(grid)
    if result:
        print(board, '=', result, 'WINS')
    else: 
        print(board, '=', 'TIE')
