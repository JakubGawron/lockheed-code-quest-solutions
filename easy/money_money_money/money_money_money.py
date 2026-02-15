import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
import math
#import string
#import re

for _ in range(int(input())):
    region = input()
    N = int(input())
    list = []
    for _ in range(N):
        PCI, year = input().split()
        PCI = math.floor((float(PCI)+500)/1000)
        year = int(year)
        list.append([year, PCI])
    
    list.sort(key=lambda k: k[0])
    print(f'{region}:')
    for year, PCI in list:
        print(year, '*'*PCI)