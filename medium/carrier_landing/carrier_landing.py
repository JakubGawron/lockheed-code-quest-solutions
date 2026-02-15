import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

def slope(x, y):
    return (y - aircraft_y) / (x - aircraft_x)

for _ in range(int(input())):
    N = int(input())
    for i in range(N):
        name = input()
        global aircraft_x, aircraft_y
        aircraft_x, aircraft_y = map(int, input().split(','))
        landingStart_x, landingStart_y = map(int, input().split(','))
        landingEnd_x, landingEnd_y = map(int, input().split(','))
        if -1.6 <= slope(landingStart_x, landingStart_y) <= -0.8 and -1.6 <= slope(landingEnd_x, landingEnd_y) <= -0.8:
            print(f'{name}, Clear To Land!')
        else:
            print(f'{name}, Abort Landing!')