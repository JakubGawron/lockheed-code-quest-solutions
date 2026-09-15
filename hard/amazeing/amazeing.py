import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re
from collections import deque

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solve_maze(maze, entrances):
    start, end = entrances
    q = deque([start + (0,)])
    vis = {start}
    while q:
        y, x, d = q.popleft()
        if (y, x) == end:
            return d // 2
        for dx, dy in dirs:
            ny, nx = y + dy, x + dx
            if (
                0 <= ny < H
                and 0 <= nx < W
                and maze[ny][nx] == " "
                and (ny, nx) not in vis
            ):
                vis.add((ny, nx))
                q.append((ny, nx, d + 1))


for _ in range(int(input())):
    H, W = map(int, input().split())
    columns = (W - 1) // 3
    W = columns * 2 + 1
    maze = []
    for _ in range(H):
        row = list(input().replace("--", "-").replace("vv", "v").replace("^^", "^"))
        skip = 0
        for i, char in enumerate(row):
            if char != " ":
                skip = 0
                continue
            if not skip:
                del row[i + 1]
                skip = 1
            else:
                skip = 0
        maze.append(row)
    entrances = []
    for y in range(H):
        for x in range(W):
            if maze[y][x] not in {">", "v", "<", "^"}:
                continue
            maze[y][x] = " "
            entrances.append((y, x))
    print(solve_maze(maze, entrances))
