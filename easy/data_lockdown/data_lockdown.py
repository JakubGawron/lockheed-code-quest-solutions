import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re
 
for _ in range(int(input())):
    records = int(input())
    for _ in range(records):
        link, size = input().split()
        size = int(size)
        
        if not link.endswith('.lmco.com'):
            if size > 1000:
                print(link, size)