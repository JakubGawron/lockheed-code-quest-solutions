import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

cases = int(input())
alphabet = input()
for _ in range(cases-1):
    cipher = [word.split('-') for word in input().split()]
    plain = [[alphabet[int(i)-1] for i in word] for word in cipher]
    print(' '.join([''.join(word) for word in plain]))