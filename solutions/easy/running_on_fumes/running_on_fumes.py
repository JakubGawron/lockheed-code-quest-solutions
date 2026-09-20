import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re

mpg = {
    4: {
        "C": 28,
        "H": 35,
        "O": 20,
    },
    6: {
        "C": 22,
        "H": 28,
        "O": 15,
    },
    8: {
        "C": 18,
        "H": 22,
        "O": 12,
    },
}
for _ in range(int(input())):
    cylinders, fuel, max_fuel, R = map(float, input().split())
    cylinders, max_fuel, R = map(int, (cylinders, max_fuel, R))
    segments = [(s, int(n)) for s, n in (input().split() for _ in range(R))]

    completable = True
    for road_type, length in segments:
        base_mpg = mpg[cylinders][road_type]
        effective_mpg = base_mpg - 0.25 * (max_fuel - fuel)
        fuel_needed = length / effective_mpg
        if fuel <= 0 or effective_mpg <= 0 or fuel_needed > fuel:
            completable = False
            break

        fuel -= fuel_needed

    print("YES" if completable else "NO")
