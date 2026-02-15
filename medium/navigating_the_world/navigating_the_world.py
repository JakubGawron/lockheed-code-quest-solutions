import sys
input = lambda: sys.stdin.readline().rstrip()
import math
#import string
#import re

for _ in range(int(input())):
    zoom, lat, long = map(float, input().split())
    zoom = int(zoom)
    x = int((long + 180) / 360 * math.pow(2, zoom))
    y = int((1 - (math.log(math.tan(math.radians(lat)) + 1 / math.cos(math.radians(lat))) / math.pi)) * math.pow(2, zoom - 1))
    print(f'http://map.lmcodequestacademy.com/{zoom}/{x}/{y}.png')