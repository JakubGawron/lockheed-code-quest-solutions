import sys
input = lambda: sys.stdin.readline().rstrip()
#import math
#import string
#import re

for _ in range(int(input())):
    failed = []
    for i in range(1, int(input())+1):
        text = input().upper()
        if text != text[::-1]:
            failed.append(str(i))
    
    if failed:
        print('False -', ', '.join(failed))
    else:
        print('True')