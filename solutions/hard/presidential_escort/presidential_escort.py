import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re
from collections import deque

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def solve(Y, X, start, end, grid):
    q = deque([start + (0,)])
    vis = {start}
    while q:
        y, x, d = q.popleft()
        if (y, x) == end:
            return d
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if (
                0 <= ny < Y
                and 0 <= nx < X
                and grid[ny][nx] == "."
                and (ny, nx) not in vis
            ):
                vis.add((ny, nx))
                q.append((ny, nx, d + 1))


for _ in range(int(input())):
    X, Y = map(int, input().split())
    grid = [list(input()) for _ in range(Y)]
    start, end = (0, 0), (0, 0)
    for y in range(Y):
        for x in range(X):
            if grid[y][x] == "P":
                grid[y][x] = "."
                start = (y, x)
            elif grid[y][x] == "D":
                grid[y][x] = "."
                end = (y, x)
    for y in range(Y):
        for x in range(X):
            if grid[y][x] not in (".", "*"):
                r = int(grid[y][x])
                grid[y][x] = "*"
                for y_r in range(max(0, y - r), min(y + r + 1, Y)):
                    for x_r in range(max(0, x - r), min(x + r + 1, X)):
                        if (y_r - y) ** 2 + (x_r - x) ** 2 <= (r + 0.5) ** 2 and grid[
                            y_r
                        ][x_r] == ".":
                            grid[y_r][x_r] = "*"
    print(solve(Y, X, start, end, grid))
