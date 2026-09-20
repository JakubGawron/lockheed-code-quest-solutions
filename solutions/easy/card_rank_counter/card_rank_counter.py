import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re

for _ in range(int(input())):
    cards = [input() for _ in range(int(input()))]
    rank = input()
    print(cards.count(rank))
