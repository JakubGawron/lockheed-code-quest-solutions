import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

colors = ['off', 'red', 'green', 'blue']
for _ in range(int(input())):
    battery, heat, water, temperature = input().split()
    battery = 8 if battery == 'BROKEN' else 0
    heat = 4 if heat == 'BROKEN' else 0
    water = 2 if water == 'BROKEN' else 0
    temperature = 1 if temperature == 'BROKEN' else 0
    sum = battery+heat+water+temperature
    num = sum-(sum%4)
    lLED = int(num / 4)
    rLED = sum - num
    print(colors[lLED], colors[rLED])