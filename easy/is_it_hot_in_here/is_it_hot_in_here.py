import sys
input = lambda: sys.stdin.readline().rstrip()
#import json
import math
#import string
#import re

for _ in range(int(input())):
    for _ in range(int(input())):
        input = input()
        temp, scale = input.split()
        temp = float(temp)

        if scale == 'F':
            temp = (5/9)*(temp-32)
            scale = 'C'
        else:
            temp = (9/5*temp)+32
            scale = 'F'
        
        print(f'{input} = {temp:.1f} {scale}')