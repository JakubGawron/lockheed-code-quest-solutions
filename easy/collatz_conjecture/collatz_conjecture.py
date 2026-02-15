import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

def collatzSeqLen(num):
    len = 1
    while num != 1:
        if num % 2 == 0:
            num = num/2
        else:
            num = num*3+1
        len += 1
    return len

for _ in range(int(input())):
    start = int(input())
    print(f'{start}:{collatzSeqLen(start)}')