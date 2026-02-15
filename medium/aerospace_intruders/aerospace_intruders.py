import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

v = {'A': 10, 'B': 20, 'C': 30}
class ship:
    def __init__(self, name, classe, x, y):
        self.name = name
        self.classe = classe
        self.x = x
        self.y = y

for _ in range(int(input())):
    enemies = []
    N = int(input())
    for _ in range(N):
        name, classe = input().split('_')
        classe, x = classe.split(':')
        x, y = map(int, x.split(','))
        enemies.append(ship(name, classe, x, y))

    for _ in range(N):
        closest = max(enemies, key=lambda e: (-e.x, e.y))
        print(f'Destroyed Ship: {closest.name} xLoc: {closest.x}')
        enemies.remove(closest)
        for s in enemies:
            s.x -= v[s.classe]