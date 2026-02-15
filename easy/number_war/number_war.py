import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

def max_2digit(numbers):
    return int(''.join(map(str, sorted(numbers, reverse=True)[:2])))

for _ in range(int(input())):
    cards = list(map(int, input().split()))
    player1, player2 = cards[:3], cards[3:]
    p1_max = max_2digit(player1)
    p2_max = max_2digit(player2)
    if p1_max > p2_max:
        print('PLAYER 1')
    elif p1_max < p2_max:
        print('PLAYER 2')
    else:
        print('WAR!')