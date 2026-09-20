import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re


def get_score(distance, speed, fuel_rate, maintenance_cost):
    time = distance / speed * 60 * 60
    fuel = distance * fuel_rate
    return time + fuel + maintenance_cost


for _ in range(int(input())):
    (
        N,
        f22_speed,
        f22_fuel_rate,
        f22_max_payload,
        f22_maintenance_cost,
        raider_speed,
        raider_fuel_rate,
        raider_max_payload,
        raider_maintenance_cost,
    ) = map(int, input().split())

    for _ in range(N):
        distance, payload = map(int, input().split())

        if payload > f22_max_payload:
            print("Sikorsky Raider")
            continue

        if payload > raider_max_payload:
            print("F-22 Raptor")
            continue

        f22_score = get_score(distance, f22_speed, f22_fuel_rate, f22_maintenance_cost)
        raider_score = get_score(
            distance, raider_speed, raider_fuel_rate, raider_maintenance_cost
        )

        if f22_score < raider_score:
            print("F-22 Raptor")
            continue

        print("Sikorsky Raider")
