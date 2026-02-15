import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
#import math
#import string
#import re

class Image:
    def __init__(self, height):
        self.height = height
        self.content = [input() for _ in range(height)]
        self.width = max(map(len, self.content)) 
    
    def flip_x(self):
        self.content = self.content[::-1]

    def flip_y(self):
        self.content = [row.ljust(self.width)[::-1] for row in self.content]
    
    def inverse(self): 
        self.content = [''.join(row.ljust(self.width)[i] for row in self.content) for i in range(self.width)]

    def show(self):
        print('\n'.join(self.content))

for _ in range(int(input())):
    image = Image(int(input()))
    mode = input()
    if mode == 'X':
        image.flip_x()
    elif mode == 'Y':
        image.flip_y()
    else:
        image.inverse()
    image.show()