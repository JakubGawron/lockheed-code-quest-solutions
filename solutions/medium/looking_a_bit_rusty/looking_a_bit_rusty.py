import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re


def next_line():
    line = input()
    while line.strip() == "":
        line = input()
    return line


def extract_quoted(line):
    i = line.find('"')
    j = line.rfind('"')
    return line[i + 1 : j]


out = []

for _ in range(int(next_line())):
    next_line()
    next_line()
    header = extract_quoted(next_line()).split()
    W, H, C, P = int(header[0]), int(header[1]), int(header[2]), int(header[3])

    colors = {}
    for _ in range(C):
        content = extract_quoted(next_line())
        ch = content[0]
        val = content[4:].strip()
        colors[ch] = val

    grid = []
    for _ in range(H):
        content = extract_quoted(next_line())
        row = []
        for ch in content[:W]:
            val = colors.get(ch, "None")
            if val.lower() == "none" or val.upper() == "#526988":
                row.append(0)
            else:
                row.append(1)
        if len(row) < W:
            row += [0] * (W - len(row))
        grid.append(row)

    dp = [[0] * W for _ in range(H)]
    max_side = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])

    out.append("FAIL" if max_side >= 2 else "PASS")

print("\n".join(out))
