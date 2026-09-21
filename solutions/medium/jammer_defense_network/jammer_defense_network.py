import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re


def is_in_range(x, y, r):
    return x**2 + y**2 <= r**2


for _ in range(int(input())):
    ally_jammers = set()
    enemy_transmiters = set()
    for _ in range(int(input())):
        tower_type, location, r, frequency = input().split()
        x, y = map(int, location.split(","))
        r = int(r)
        frequency = int(frequency)

        if is_in_range(x, y, r):
            match tower_type:
                case "J":
                    ally_jammers.add(frequency)
                case "T":
                    enemy_transmiters.add(frequency)

    if enemy_transmiters - ally_jammers == set():
        print("SAFE")
        continue

    print("UNSAFE")
