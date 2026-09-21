import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re

for _ in range(int(input())):
    N, P = map(int, input().split())
    printers = {
        printer: (float(density), float(mass))
        for printer, density, mass in (input().split() for _ in range(N))
    }

    for _ in range(P):
        id, volume, infill = input().split()
        volume = int(volume)
        infill = float(infill)

        density, mass = printers[id]

        print(int(mass // (volume * infill * density)))
