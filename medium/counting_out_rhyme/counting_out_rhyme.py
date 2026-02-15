import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

def josephus(N, K):
    if (N == 1):
        return 1
    else:
        return (josephus(N - 1, K) + K - 1) % N + 1
        
for _ in range(int(input())):
    N, K = map(int, input().split())
    print(list(range(1, N+1))[1 - josephus(N, K)])
    