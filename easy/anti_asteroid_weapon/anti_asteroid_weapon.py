import sys
input = lambda: sys.stdin.readline().rstrip()
import math
#import string
#import re

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def __repr__(self):
        return f'{self.x} {self.y}'
    
for test in range(int(input())):
    asteroids = int(input())
    points = []
    for asteroid in range(asteroids):
        x, y = map(int, input().split())
        points.append(Point(x, y))

    points.sort(key=lambda point: point.distance())
    for point in points:
        print(repr(point))