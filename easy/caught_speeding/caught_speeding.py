import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    speed, isBirthday = input().split()
    speed = int(speed)
    isBirthday = 1 if isBirthday == 'true' else 0
    
    if speed <= 60+isBirthday*5:
        print('no ticket')
    elif speed >= 61+isBirthday*5 and speed <= 80+isBirthday*5:
        print('small ticket')
    else:
        print('big ticket')