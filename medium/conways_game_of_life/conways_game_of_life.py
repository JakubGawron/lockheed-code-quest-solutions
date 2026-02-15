import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

def countNeighbors(x, y):
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    counter = 0
    for tx, ty in neighbors:
        tx += x
        ty += y
        if 0 <= tx <= 9 and 0 <= ty <= 9:
            counter += int(world[ty][tx])
    return counter

def redrawWorld():
    newWorld = []
    for y in range(10):
        row = ''
        for x in range(10):
            neighbors = countNeighbors(x, y)
            if neighbors <= 1:
                row += '0'
            elif neighbors < 3:
                if world[y][x] == '1':
                    row += '1'
                else:
                    row += '0'
            elif neighbors >= 4:
                row += '0'
            elif neighbors == 3:
                row += '1'
        newWorld.append(row)
    return newWorld

for _ in range(int(input())):
    world = []
    X = int(input())
    for _ in range(10):
        world.append(input())
    
    for _ in range(X):
        world = redrawWorld()
    print('\n'.join(world))