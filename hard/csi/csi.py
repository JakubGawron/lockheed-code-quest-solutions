import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

def lcs(a, b):
    dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

for _ in range(int(input())):
    found = input()
    database = [input().split('=') for _ in range(int(input()))]
    print(max(database, key=lambda k: lcs(found, k[1]))[0])
        