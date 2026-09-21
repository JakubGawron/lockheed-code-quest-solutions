import sys

input = lambda: sys.stdin.readline().rstrip()
import math

# import string
# import re


for _ in range(int(input())):
    states = {}
    seats = {}

    for _ in range(50):
        (
            state,
            population,
        ) = input().split()
        population = int(population)
        states[state] = population
        seats[state] = 1

    for _ in range(435 - 50):
        priorities = {}

        for state, population in states.items():
            n = seats[state] + 1
            multiplier = 1 / math.sqrt(n * (n - 1))
            priority = population * multiplier
            priorities[state] = priority

        max_state = max(priorities, key=priorities.get)
        seats[max_state] += 1

    for state in sorted(seats.keys()):
        print(f"{state} {seats[state]}")
