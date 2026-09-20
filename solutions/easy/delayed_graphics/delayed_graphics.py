import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re

for _ in range(int(input())):
    max_delay = int(input())
    delays = sum(map(int, input().split()))
    diffrence = max_delay - delays
    if diffrence < 0:
        print(abs(diffrence))
        continue
    print("PASS")
