import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    board = input().split()

    indexes = []
    for _ in range(9):
        if 'M' in board:
            i = board.index('M')
            board[i] = ''
            indexes.append(str(i+1))
    print(' '.join(indexes))