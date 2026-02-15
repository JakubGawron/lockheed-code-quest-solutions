import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    name, timeList = input().split(',', 1)
    timeList = timeList.split(',')
    h, m = 0, 0
    for time in timeList:
        h += int(time[:2])
        m += int(time[3:])
    
    h, m = h+m//60, m%60


    print(f'{name}={h+m//60} hour', end='')
    if h != 1:
        print('s', end='') 
    if m != 0:
        print(f' {m%60} minute', end='')
        if m != 1:
            print('s', end='')
    print()