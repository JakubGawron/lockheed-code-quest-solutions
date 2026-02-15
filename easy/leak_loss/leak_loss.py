import sys
input = lambda: sys.stdin.readline().rstrip()
import math
#import string
#import re

for _ in range(int(input())):
    VOP, ROF, ROL = map(int, input().split())
    print(math.floor((VOP/(ROF-ROL)*ROL)+0.5))
