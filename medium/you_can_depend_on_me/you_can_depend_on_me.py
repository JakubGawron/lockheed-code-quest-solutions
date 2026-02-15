import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re
from collections import defaultdict, deque

def get_levels(root, tree):
    queue = deque([(root, 0)])
    levels = defaultdict(list)
    visited = set()
    while queue:
        node, depth = queue.popleft()
        if node in visited: continue
        visited.add(node)
        levels[depth].append(node)
        for child in tree[node]:
            queue.append((child, depth + 1))
    return [sorted(level) for level in levels.values()][::-1]

programs = {}
for _ in range(int(input())):
    programs = defaultdict(list)
    D, E = map(int, input().split())
    for _ in range(D):
        k, v = input().split()
        programs[k].append(v)
        if v not in programs: programs[v] = []

    for _ in range(E):
        for level in get_levels(input(), programs):
            for program in level:
                print('restart', program)
        print('exit')