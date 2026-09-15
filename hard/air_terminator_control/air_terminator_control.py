import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re


def get_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes


for _ in range(int(input())):
    friendly, N = input().split()
    friendly = friendly == "TRUE"
    N = int(N)
    times = [input() for _ in range(N)]
    threat = "NONE"
    if not friendly:
        last_minutes = get_minutes(times[0])
        max_continuous, continuous, occasions = 0, 1, 1
        for time in times[1:]:
            minutes = get_minutes(time)
            diff = minutes - last_minutes
            if diff < 0:
                diff += 24 * 60
            if diff == 15:
                continuous += 1
            else:
                max_continuous = max(max_continuous, continuous)
                continuous = 1
                occasions += 1
            last_minutes = minutes
        max_continuous = max(max_continuous, continuous)

        if N >= 36 or max_continuous >= 12 or occasions >= 8:
            threat = "HIGH"
        elif N >= 24 or max_continuous >= 8 or occasions >= 4:
            threat = "MEDIUM"
        elif N >= 12 or max_continuous >= 4:
            threat = "LOW"

    print(threat)
