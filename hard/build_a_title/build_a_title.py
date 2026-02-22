import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

def get_overlap(a, b):
    for i in range(min(len(a), len(b)), 0, -1):
        if a.endswith(b[:i]):
            return i
    return 0

def get_longest_title(titles, n):
    overlaps = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if y != x:
                 overlaps[y][x] = get_overlap(titles[y], titles[x])
    
    longest = ''
    def dfs(title, j, used):
        nonlocal longest
        if len(title) > len(longest) or (len(title) == len(longest) and title < longest):
            longest = title

        for i in range(n):
            if used[i]: continue
            overlap = overlaps[j][i]
            if overlap == 0: continue

            new_title = title + titles[i][overlap:]
            used[i] = 1
            dfs(new_title, i, used)
            used[i] = 0

    for i in range(n):
        used = [0] * n
        used[i] = 1
        dfs(titles[i], i, used)

    return longest

for _ in range(int(input())):
    n = int(input())
    titles = [input() for _ in range(n)]
    print(get_longest_title(titles, n))