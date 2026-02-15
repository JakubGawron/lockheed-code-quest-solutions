import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    agents = {}
    for agent in input().split():
        name, score = agent.split('=')
        agents[name] = int(score)

    g = []
    max_len = 0
    for i in range(1, 90+1):
        t =  [name for name, score in agents.items() if i <= score <= i+10]
        if t not in g:
            if len(t) > max_len:
                max_len = len(t)
                g = []
                g.append(sorted(t))
            elif len(t) == max_len:
                g.append(sorted(t))
    print(' '.join(sorted(g)[0]))