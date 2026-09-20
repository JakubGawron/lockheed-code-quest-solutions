import sys

input = lambda: sys.stdin.readline().rstrip()
import math

# import string
# import re


for _ in range(int(input())):
    total_length, pace = input().split()
    total_length = float(total_length)
    minutes, seconds = map(int, pace.split(":"))
    average_pace = minutes + seconds / 60
    fast_pace = average_pace - 1
    slow_pace = average_pace + 1
    interval_distance = 5 / fast_pace + 5 / slow_pace
    intervals = math.floor((total_length - 2) / interval_distance)

    print(max(1, intervals))
