import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

for _ in range(int(input())):
    temp, water, magn, ecce = input().split()
    temp = float(temp)
    ecce = float(ecce)
    water = 1 if water == 'true' else 0
    magn = 1 if magn == 'true' else 0

    if temp > 100:
        print('The planet is too hot.')
    elif temp < 0:
        print('The planet is too cold.')
    elif not water:
        print('The planet has no water.')
    elif not magn:
        print('The planet has no magnetic field.')
    elif ecce > 0.6:
        print("The planet's orbit is not ideal.")
    else:
        print('The planet is habitable.')