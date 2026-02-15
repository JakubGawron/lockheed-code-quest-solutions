import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
import math
#import string
#import re

for _ in range(int(input())):
    launched = 0
    for _ in range(int(input())):
        date, time, cloudThic, windspeed, windDirection = input().split()
        cloudThic, windspeed, windDirection = int(cloudThic), float(windspeed), int(windDirection)
        windEw = abs(windspeed * math.sin(math.radians(windDirection)))
        windNs = abs(windspeed * math.cos(math.radians(windDirection)))
        if cloudThic <= 1000 and windNs <= 20 and windEw <= 40 and not launched:
            print(date, time)
            launched = 1
    if not launched:
        print('ABORT LAUNCH')