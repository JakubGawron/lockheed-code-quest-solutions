import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

def lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [0] * (n + 1)
    for i in range(1, m + 1):
        previous = dp[0]
        for j in range(1, n + 1):
            temporary = dp[j]
            if s1[i - 1] == s2[j - 1]:
                dp[j] = 1 + previous
            else:
                dp[j] = max(dp[j - 1], dp[j])
            previous = temporary
    return dp[n]

for _ in range(int(input())):
    found = input()
    database = [[d[0], lcs(found, d[1])] for d in (input().split('=') for _ in range(int(input())))]
    max_lcs = max(database, key=lambda k: k[1])[1]
    closest = sorted(person[0] for person in database if person[1] == max_lcs)
    print(','.join(closest))