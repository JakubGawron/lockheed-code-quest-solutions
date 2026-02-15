import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.read = 0
        self.count = 0

    def overfit(self, a, b):
        return (a + b) % self.size

    def __add__(self, elements):
        for el in elements:
            if self.count < self.size:
                self.buffer[self.overfit(self.read, self.count)] = el
                self.count += 1
            else:
                self.buffer[self.read] = el
                self.read = self.overfit(self.read, 1)

    def __consume__(self, n: int):
        if n >= self.count:
            self.read = 0
            self.count = 0
            return

        self.read = self.overfit(self.read, n)
        self.count -= n

    def __show__(self):
        if self.count == 0:
            print("Empty")
            return

        if self.count % 2 == 1:
            mid = self.count // 2
            print(self.buffer[self.overfit(self.read, mid)])
        else:
            mid = self.count // 2
            print(self.buffer[self.overfit(self.read, mid - 1)], self.buffer[self.overfit(self.read, mid)])

for _ in range(int(input())):
    N, S = map(int, input().split())
    cb = CircularBuffer(S)

    for _ in range(N):
        command = input().split(maxsplit=1)
        if command[0] == 'ADD': cb.__add__(command[1].split())
        
        elif command[0] == 'CONSUME': cb.__consume__(int(command[1]))

        elif command[0] == 'SHOW': cb.__show__()